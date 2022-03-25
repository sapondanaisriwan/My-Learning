import asyncio
import itertools
from datetime import timedelta
from functools import partial

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
from discord.utils import get

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}


ffmpeg_options = {'options': '-vn',
                  "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"}


ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.thumbnail = data.get('thumbnail')
        self.channel = data.get('channel')
        self.duration = data.get('duration')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        # send an embed
        emBed = discord.Embed(
            title=data['title'], url=data['webpage_url'], color=0x30d96b)
        emBed.set_thumbnail(url=data['thumbnail'])
        emBed.add_field(name='Channel', value=data['channel'], inline=True)
        emBed.add_field(name='Duration', value=str(
            timedelta(seconds=data['duration'])), inline=True)
        emBed.set_author(name='Added to queue',
                         icon_url=ctx.message.author.display_avatar)

        # await ctx.send(embed=emBed, delete_after=15)
        await ctx.send(embed=emBed)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source, **ffmpeg_options), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info,
                         url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options), data=data, requester=requester)


class MusicPlayer:
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', '_message',
                 '_author', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        # print('ctx=\n' + str(dir(ctx)))
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog
        self._message = ctx.message
        self._author = ctx.author
        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(30):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'There was an error processing your song.\n'f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(
                source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

            try:
                pass
                # We are no longer playing this song...
                # await self.np.delete()
            except discord.HTTPException:
                pass

    async def destroy(self, guild):
        """Disconnect and cleanup the player."""
        try:
            del players[self._guild]
            await self._guild.voice_client.disconnect()
            return self.bot.loop.create_task(self._cog.cleanup(guild))
        except:
            print('error')


players = {}


def get_player(ctx):
    try:
        player = players[ctx.guild.id]
    except:
        player = MusicPlayer(ctx)
        players[ctx.guild.id] = player
    return player


class Music_Commands(commands.Cog, name='Music commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play', aliases=['p'], help='Plays an audio resource right in your voice channel.')
    async def _play(self, ctx, *, search: str):  # ctx = คนใช้คำสั่ง/ผู้ใช้

        channel = ctx.author.voice.channel
        emBed = discord.Embed(color=0xff0000)
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)

        if ctx.author.voice == None:
            emBed.set_author(
                name=" | You're not in a voice channel",
                icon_url=ctx.message.author.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client == None:
            await channel.connect()
            voice_client = get(self.bot.voice_clients, guild=ctx.guild)

        if voice_client.channel != ctx.author.voice.channel:  # ห้องของบอทไมไ่ด้อยู่ห้องเดียวกับผู้ใช้
            return await ctx.channel.send(f"❌ **| You're not in the same voice channel with me. Please join** <#{voice_client.channel.id}>")

        _player = get_player(ctx)
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await _player.queue.put(source)

    """Pause music"""

    @commands.command(help='Pauses the music playback if playing')
    async def pause(self, ctx):

        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        if ctx.author.voice == None:  # if user not in the vc
            emBed = discord.Embed(color=0xff0000)
            emBed.set_author(
                name=" | You're not in a voice channel",
                icon_url=ctx.message.author.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client == None:  # ถ้าบอทยังไม่ได้อยู่ใน vc ไหนเลย ระหว่างกับผู้ใช้อยู่ใน vc // ผู้ใช้ยังไม่ได้ใช้ command play //  there is nothing playing on this guild
            emBed = discord.Embed(color=0xff0000)
            emBed.set_author(
                name=" | There is nothing playing on this guild",
                icon_url=self.bot.user.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client.channel != ctx.author.voice.channel:  # ห้องของบอทไมไ่ด้อยู่ห้องเดียวกับผู้ใช้

            return await ctx.channel.send(f"❌ **| You're not in the same voice channel with me. Please join** <#{voice_client.channel.id}>")

        emBed = discord.Embed(description="Paused the song.", color=0x00ff00)
        await ctx.send(embed=emBed)
        voice_client.pause()

    @commands.command(help='Resumes the music playback if paused')
    async def resume(self, ctx):

        emBed = discord.Embed(color=0xff0000)
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)

        if ctx.author.voice == None:  # if user not in the vc
            emBed.set_author(
                name=" | You're not in a voice channel",
                icon_url=ctx.message.author.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client == None:
            emBed.set_author(
                name=" | Bot is not connected to voice channel yet",
                icon_url=self.bot.user.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client.channel != ctx.author.voice.channel:  # channel ของ bot != คนพิมพ์
            return await ctx.channel.send(f"❌ **| You're not in the same voice channel with me. Please join** <#{voice_client.channel.id}>")

        emBed = discord.Embed(
            description="Resumed the song.",
            color=0x00ff00
        )

        await ctx.send(embed=emBed)
        voice_client.resume()

    @commands.command(name='leave', aliases=['stop', 'dis', 'disconnect'])
    async def _leave(self, ctx):

        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        emBed = discord.Embed(color=0xff0000)

        if ctx.author.voice == None:  # if user not in the vc
            emBed.set_author(
                name=" | You're not in the voice channel",
                icon_url=ctx.message.author.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client == None:  # bot ไม่อยู่ใน vc
            emBed.set_author(
                name=" | There's nothing playing in this server",
                icon_url=self.bot.user.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client.channel != ctx.author.voice.channel:  # ห้องของบอทไมไ่ด้อยู่ห้องเดียวกับผู้ใช้
            return await ctx.send(f" ❌ **| You're not in the same voice channel with me. Please join** <#{voice_client.channel.id}>")

        if ctx.voice_client:  # If the bot is in a voice channel
            del players[ctx.guild.id]
            await ctx.voice_client.disconnect()
            await ctx.message.add_reaction('👌')

    @commands.command(name='queue', aliases=['q'], help='Shows the queued songs in this server')
    async def _queueList(self, ctx):

        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        emBed = discord.Embed(color=0xff0000)

        if ctx.author.voice == None:  # if user not in the vc
            emBed.set_author(
                name=" | You're not in a voice channel",
                icon_url=ctx.message.author.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client == None:
            emBed.set_author(
                name=" | Bot is not connected to voice channel yet",
                icon_url=self.bot.user.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client.channel != ctx.author.voice.channel:  # channel ของ bot != คนพิมพ์
            return await ctx.channel.send(f"❌ **| You're not in the same voice channel with me. Please join** <#{voice_client.channel.id}>")

        player = get_player(ctx)
        if player.queue.empty():
            return await ctx.send("❌ **| There's no song in the queue**")

        # 1 2 3
        upcoming = list(itertools.islice(
            player.queue._queue, 0, player.queue.qsize()))
        embed = discord.Embed(
            title=f"**Queue for {ctx.guild}**",
            description=f"**Next Coming**",
        )
        queueList = 1

        for song in upcoming:
            embed.description += f"\n{queueList}.) [{song['title']}]({song['webpage_url']}) | Requested by <@{song['requester'].id}>"
            queueList += 1

        await ctx.send(embed=embed)

    @commands.command(name='skip', aliases=['s'], help='Skips the current playing song in track or skips the number of songs you specified in track.')
    async def _skip(self, ctx):

        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        emBed = discord.Embed(color=0xff0000)

        if ctx.author.voice == None:  # if user not in the vc
            emBed.set_author(
                name=" | You're not in a voice channel",
                icon_url=ctx.message.author.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client == None:  # if the
            emBed.set_author(
                name=" | Bot is not connected to voice channel yet",
                icon_url=self.bot.user.display_avatar
            )
            return await ctx.send(embed=emBed)

        if voice_client.channel != ctx.author.voice.channel:  # channel ของ bot != คนพิมพ์
            return await ctx.channel.send(f"❌ **| You're not in the same voice channel with me. Please join** <#{voice_client.channel.id}>")

        if voice_client.is_paused():
            pass  # continueo
        elif not voice_client.is_playing():
            return

        voice_client.stop()
        await ctx.message.add_reaction('👌')


def setup(bot):
    bot.add_cog(Music_Commands(bot))
