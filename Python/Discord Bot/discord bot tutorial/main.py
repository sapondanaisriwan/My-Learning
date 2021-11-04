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
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)


"""
CLIENT EVENT
"""

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    print(message.content)
    if message.author.bot:
        return

# detect deleted message
@client.event
async def on_message_delete(message):

    if message.author.bot:
        return

    if message.content: # to ignore the error if user send an image
        await message.channel.send(message.content)


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def clear(ctx, amount=5):

    if ctx.author.bot:
        return

    await ctx.channel.purge(limit=amount+1)

client.run(TOKEN)

