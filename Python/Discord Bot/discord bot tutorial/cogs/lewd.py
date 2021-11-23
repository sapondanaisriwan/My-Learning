import random
from datetime import datetime

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from waifu import WaifuAioClient

waifu = WaifuAioClient()

class Lewd_Commands(commands.Cog, name='Lewd commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Grabs a randomized lewdwaifu image/gif")
    @commands.is_nsfw()
    async def lewdwaifu(self, ctx):
        nsfw_lewdwaifu = await waifu.nsfw(category='waifu')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=nsfw_lewdwaifu)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized lewdneko image/gif")
    @commands.is_nsfw()
    async def lewdneko(self, ctx):
        nsfw_neko = await waifu.nsfw(category='neko')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=nsfw_neko)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized blowjob image/gif")
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        nsfw_blowjob = await waifu.nsfw(category='blowjob')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=nsfw_blowjob)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(help="Grabs a randomized Trap image/gif")
    @commands.is_nsfw()
    async def trap(self, ctx):
        nsfw_trap = await waifu.nsfw(category='trap')

        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url=nsfw_trap)
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f"{ctx.author.avatar_url}"
        )
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command()
    async def nhentai(self, ctx):
        url = 'https://nhentai.to/random/'
        web_data = requests.get(url)
        soup = BeautifulSoup(web_data.text, 'html.parser')
        find_word = soup.find_all('img')
        test = []
        for i in find_word:
            i = i.get('src')
            if i is not None:
                print(i)
                test.append(i)
        random_doujin = random.choice(test)
        print(random_doujin)
        await ctx.send(random_doujin)

def setup(bot):
    bot.add_cog(Lewd_Commands(bot))
