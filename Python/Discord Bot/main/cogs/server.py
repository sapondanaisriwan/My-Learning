from os import name
import discord
from discord.ext import commands


class Server(commands.Cog, name='Server commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='yrugay', show_hidden=True)
    async def wrug(self, ctx):
        await ctx.send('Why r u gay')

    # HERE
    # HERE
    # HERE
    # HERE
    # HERE
    # HERE
    # HERE
    # HERE
    # HERE
    # HERE


    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('member.json', 'w') as file:
            # tomorrow you need to do more:
            # 1.add user name to json 
            # 2.reset the user name
            # 3.save all the member's name
            await member.edit('No Name')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')


def setup(bot):
    bot.add_cog(Server(bot))
