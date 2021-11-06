#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \|     |// '.
#                  / \|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
PREFIX = "."
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

"""
Catch error message
"""

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.MemberNotFound):
        await ctx.send(f"MemberNotFound: {error}")

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Error: {error}")

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'CommandInvokeError {error}')

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing a required argument.")

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to run this command.")
    
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have sufficient permissions!")

    else:
        print(error)


@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

if __name__ == '__main__':

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')



# @bot.event
# async def on_message(message):

#     if message.author.bot:
#         return
    
#     await bot.process_commands(message)


# # detect deleted message
# @bot.event
# async def on_message_delete(message):

#     if message.author.bot:
#         return

#     if message.content: # to ignore the error if user send an image
#         await message.channel.send(message.content)

bot.run(TOKEN)

