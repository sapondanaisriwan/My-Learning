import discord
from discord.ext import commands

class Server(commands.Cog, name='Server commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='yrugay', show_hidden = True)
    async def wrug(self, ctx):
        await ctx.send('Why r u gay')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')


def setup(bot):
    bot.add_cog(Server(bot))
