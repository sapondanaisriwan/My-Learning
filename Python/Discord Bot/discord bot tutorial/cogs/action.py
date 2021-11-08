from datetime import datetime

import discord
from discord.ext import commands
from waifu import WaifuAioClient

waifu = WaifuAioClient()


class ActionCommand(commands.Cog, name='Action commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Grabs a randomized waifu image/gif")
    async def waifu(self, ctx):
        sfw_waifu = await waifu.sfw(category='waifu')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_waifu)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized neko image/gif")
    async def neko(self, ctx):
        sfw_neko = await waifu.sfw(category='neko')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_neko)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized shinobu image/gif")
    async def shinobu(self, ctx):
        sfw_shinobu = await waifu.sfw(category='shinobu')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_shinobu)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized megumin image/gif")
    async def megumin(self, ctx):
        sfw_megumin = await waifu.sfw(category='megumin')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_megumin)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized bully image/gif")
    async def bully(self, ctx):
        sfw_bully = await waifu.sfw(category='bully')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_bully)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized cuddle image/gif")
    async def cuddle(self, ctx):
        sfw_cuddle = await waifu.sfw(category='cuddle')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_cuddle)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized cry image/gif")
    async def cry(self, ctx):
        sfw_cry = await waifu.sfw(category='cry')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_cry)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)
    
    @commands.command(help="Grabs a randomized hug image/gif")
    async def hug(self, ctx):
        sfw_hug = await waifu.sfw(category='hug')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_hug)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized awoo image/gif")
    async def awoo(self, ctx):
        sfw_awoo = await waifu.sfw(category='awoo')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_awoo)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized kiss image/gif")
    async def kiss(self, ctx):
        sfw_kiss = await waifu.sfw(category='kiss')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_kiss)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized lick image/gif")
    async def lick(self, ctx):
        sfw_lick = await waifu.sfw(category='lick')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_lick)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized pat image/gif")
    async def pat(self, ctx):
        sfw_pat = await waifu.sfw(category='pat')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_pat)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized smug image/gif")
    async def smug(self, ctx):
        sfw_smug = await waifu.sfw(category='smug')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_smug)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized bonk image/gif")
    async def bonk(self, ctx):
        sfw_bonk = await waifu.sfw(category='bonk')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_bonk)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized yeet image/gif")
    async def yeet(self, ctx):
        sfw_yeet = await waifu.sfw(category='yeet')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_yeet)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized blush image/gif")
    async def blush(self, ctx):
        sfw_blush = await waifu.sfw(category='blush')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_blush)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized smile image/gif")
    async def smile(self, ctx):
        sfw_smile = await waifu.sfw(category='smile')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_smile)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized wave image/gif")
    async def wave(self, ctx):
        sfw_wave = await waifu.sfw(category='wave')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_wave)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized highfive image/gif")
    async def highfive(self, ctx):
        sfw_highfive = await waifu.sfw(category='highfive')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_highfive)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized handhold image/gif")
    async def handhold(self, ctx):
        sfw_handhold = await waifu.sfw(category='handhold')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_handhold)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized nom image/gif")
    async def nom(self, ctx):
        sfw_nom = await waifu.sfw(category='nom')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_nom)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized bite image/gif")
    async def bite(self, ctx):
        sfw_bite = await waifu.sfw(category='bite')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_bite)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized glomp image/gif")
    async def glomp(self, ctx):
        sfw_glomp = await waifu.sfw(category='glomp')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_glomp)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized slap image/gif")
    async def slap(self, ctx):
        sfw_slap = await waifu.sfw(category='slap')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_slap)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized kill image/gif")
    async def kill(self, ctx):
        sfw_kill = await waifu.sfw(category='kill')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_kill)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)     
    
    @commands.command(help="Grabs a randomized happy image/gif")
    async def happy(self, ctx):
        sfw_happy = await waifu.sfw(category='happy')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_happy)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized wink image/gif")
    async def wink(self, ctx):
        sfw_wink = await waifu.sfw(category='wink')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_wink)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized poke image/gif")
    async def poke(self, ctx):
        sfw_poke = await waifu.sfw(category='poke')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_poke)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)    
    
    @commands.command(help="Grabs a randomized dance image/gif")
    async def dance(self, ctx):
        sfw_dance = await waifu.sfw(category='dance')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_dance)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized cringe image/gif")
    async def cringe(self, ctx):
        sfw_cringe = await waifu.sfw(category='cringe')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=sfw_cringe)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)
    

def setup(bot):

    bot.add_cog(ActionCommand(bot))
