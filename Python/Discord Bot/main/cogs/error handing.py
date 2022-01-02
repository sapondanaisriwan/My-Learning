from os import error
import discord
from discord.ext import commands
class Error(commands.Cog, command_attrs=dict(hidden=True)):

    def __init__(self, bot) -> None:
        bot.self = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"MemberNotFound: {error}")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Error: {error}")

        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f'CommandInvokeError {error}')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.command)
            # await ctx.send(f"Missing a required argument.")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions to run this command.")
        
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have sufficient permissions!")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'This command is on cooldown. Please wait {error.retry_after:2f}s')

def setup(bot):
    bot.add_cog(Error(bot))