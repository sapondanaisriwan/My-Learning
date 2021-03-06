import io
from datetime import datetime
from logging import error

import discord
from numpy import append
import pyshorteners
import qrcode
from discord.ext import commands
from googletrans import Translator


class Userful(commands.Cog, name='Useful commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='members', aliases=['getuser'], help='Gets the info of the server where this command is invoked.')
    @commands.has_permissions(manage_guild=True)
    async def get_members(self, ctx):
        # await ctx.send(file=discord.File(io.BytesIO("meme"), filename="meme.txt"))

        if ctx.author.bot:
            return

        for member in ctx.guild.members:
            if str(member.nick).lower().replace(' ', '') == 'noname':
                # await member.edit(nick="឵឵ No Name")
                embed = discord.Embed(
                    description=f'Nickname was changed to {member.mention}.'
                )
                await member.edit(nick="឵឵ No Name")
                await ctx.send(embed=embed)

        # embed = discord.Embed(
        #     description=f'Nickname was changed to {member.mention}.'
        # )

        # await member.edit(nick="឵឵ No Name")
        # await ctx.send(embed=embed)

        # with open("result.txt", "w") as file:
        #     file.write(str(members))
        # await ctx.send(file=discord.File(io.BytesIO("meme"), filename="meme.txt"))
        # # send file to Discord in message
        # with open("result.txt", "rb") as file:
        #     await ctx.send("Your file is:", file=discord.File(file, "result.txt"))

    @ commands.command(name='serverinfo', aliases=['guildinfo'], help='Gets the info of the server where this command is invoked.')
    @ commands.has_permissions(manage_guild=True)
    async def server_info(self, ctx):
        guild = ctx.guilds

        embed = discord.Embed(
            title=":gear: Server Information",
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(
            name="Server Name",
            value=f'```{guild.name}```',
            inline=True
        )
        embed.add_field(
            name="Created at",
            value=f'```{guild.created_at.strftime("%d %b %Y")}```',
            inline=True
        )
        embed.add_field(
            name="Owner",
            value=f'```{guild.owner}```',
            inline=True
        )
        embed.add_field(
            name="All Members",
            value=f'```{guild.member_count}```',
            inline=True
        )
        embed.add_field(
            name="All Channels",
            value=f'```{len(guild.channels)}```',
            inline=True
        )
        embed.add_field(
            name="All Roles",
            value=f'```{len(guild.roles)}```',
            inline=True
        )
        embed.set_footer(
            text=f"Requsted By: {ctx.author}",
            icon_url=ctx.author.display_avatar
        )
        await ctx.send(embed=embed)

    @ commands.command(help='Gets the info of the user that you mention')
    async def userinfo(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        embed = discord.Embed(
            color=member.color,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=f"{member} ({member.id})",
            icon_url=f"{member.display_avatar}"
        )
        embed.add_field(
            name="Created at:",
            value=member.created_at.strftime("%d %b %Y"),
            inline=True
        )
        embed.add_field(
            name="Joined at:",
            value=member.joined_at.strftime("%d %b %Y"),
            inline=True
        )
        embed.add_field(
            name="Highest role:",
            value=member.top_role.mention,
            inline=False
        )
        embed.add_field(
            name=f"Roles Obtained ({len(roles)})",
            value=', '.join([role.mention for role in roles][1:]),
            inline=False
        )

        embed.set_thumbnail(
            url=member.display_avatar
        )
        embed.set_footer(
            text=f"Requsted By: {ctx.author}",
            icon_url=ctx.author.display_avatar
        )

        await ctx.send(embed=embed)

    @ commands.command(help='Let you clear the messages')
    @ commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx, amount: int):

        if ctx.author.bot:
            return

        await ctx.channel.purge(limit=amount + 1)

    @ commands.command(name='change', help='Convert message written in ENG to TH.')
    async def change_Language(self, ctx, *, message):

        if ctx.author.bot:
            return

        dic3 = {'a': 'ฟ', 'b': 'ิ', 'c': 'แ', 'd': 'ก', 'e': 'ำ', 'f': 'ด', 'g': 'เ', 'h': '้', 'i': 'ร', 'j': '่', 'k': 'า', 'l': 'ส', 'm': 'ท', 'n': 'ื', 'o': 'น', 'p': 'ย', 'q': 'ๆ', 'r': 'พ', 's': 'ห', 't': 'ะ', 'u': 'ี', 'v': 'อ', 'w': 'ไ', 'x': 'ป', 'y': 'ั', 'z': 'ผ',
                'A': 'ฤ', 'B': 'ฺ', 'C': 'ฉ', 'D': 'ฏ', 'E': 'ฎ', 'F': 'โ', 'G': 'ฌ', 'H': '็', 'I': 'ณ', 'J': '๋', 'K': 'ษ', 'L': 'ศ', 'M': 'ฦ', 'N': '์', 'O': 'ฯ', 'P': 'ญ', 'Q': '๐', 'R': 'ฑ', 'S': 'ฆ', 'T': 'ธ', 'U': '๊', 'V': 'ฮ', 'W': '.', 'X': ')', 'Y': 'ํ', 'Z': '(',
                '1': 'ๅ', '2': 'ฝ', '3': 'ข', '4': 'ภ', '5': 'ถ', '6': 'ุ', '7': 'ึ', '8': 'ค', '9': 'ต', '0': 'จ', '-': 'ข', '=': 'ช', '!': '๙', '@': '๑', '#': '๒', '$': '๓', '%': '๔', '^': 'ู', '&': '฿',
                '*': '๕', '(': '๖', ')': '๗', '_': '๘', '+': '๙', ';': 'ว', ',': 'ม', '[': 'บ', "'": 'ง', "\\": 'ฃ', '|': 'ฅ', '/': 'ฝ', '<': 'ฒ', '>': 'ฬ', '.': 'ใ', '?': 'ฦ', '//': 'ฝ', '?': 'ฝ', ':': 'ซ', '"': '.', '[': 'บ', ']': 'ล', '{': 'ฐ', '}': ','
                }

        for wordEN, wordTH in dic3.items():
            message = message.replace(wordEN, wordTH)
        await ctx.reply(message)

    @ commands.command()
    async def botinfo(self, ctx):
        await ctx.send(self.bot.appinfo.owner)

    @ commands.command(aliases=['qr'], help='Qrcode generator .')
    async def qrcode(self, ctx, *, url):
        try:
            q = qrcode.make(url)
            arr = io.BytesIO()
            q.save(arr, format="PNG")
            arr.seek(0)
            await ctx.send(file=discord.File(fp=arr, filename="image.png"))
        except Exception as er:
            print(er)

    @ commands.command(aliases=['t', 'tsl'], help='Translate to Thai')
    async def translate(self, ctx, *, message):

        translator = Translator()
        result = translator.translate(message, dest='th').text

        embed = discord.Embed(color=0x74d9fb)
        embed.set_author(
            name="แปลภาษา",
            icon_url="https://www.aniaetleprogrammeur.com/wp-content/uploads/2019/02/Google_Translate_Icon.png"
        )
        embed.add_field(
            name='แปลประโยค',
            value=f'```diff\n{message}```',
            inline=False
        )
        embed.add_field(
            name='ความหมาย',
            value=f'```yaml\n{result}```',
            inline=False
        )
        embed.set_footer(text=f'cr.code design by : LuckyToT#1251')

        await ctx.send(embed=embed)

    @ commands.command(help='Short url generator')
    async def shorturl(self, ctx, *, url):
        try:
            short = pyshorteners.Shortener(
                api_key='8a3dd0b5d316c0d888b0030dfbb4c8ceeaa3a3e0')
            short_url = short.bitly.short(url)
            await ctx.reply(short_url)
        except:
            pass


def setup(bot):
    bot.add_cog(Userful(bot))
