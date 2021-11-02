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

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(f"{author} {content}")

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    await message.channel.send(content)

client.run(TOKEN)

