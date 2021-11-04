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

client = commands.Bot(command_prefix='!', intents=intents)


"""
CLIENT EVENT
"""

@client.event
async def on_ready():
    print('Bot is ready')

# @client.event
# async def on_message(message):
#     client = message.channel
#     if message.content.startswith('.ping'):
#         await client.send('pong')

#     if message.content.startswith('.echo'):
#         msg = message.content.split() # ['.echo', 'hello', 'world', 'barrier']
#         msg = msg[1:] # ['hello', 'world', 'barrier']
#         output = ''
#         for word  in msg:
#             output += word
#             output += ' '
#         await client.send(output)

# detect deleted message
@client.event
async def on_message_delete(message):
    content = message.content
    await message.channel.send(content)


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# @client.command(aliases=['clear'])
# async def clear(ctx, amount = 100):
    # print('here')
    # channel = ctx.message.channel
    # messages = []
    # async for message in client.logs_form(channel, limit=int(amount)):
    #     print(message)
    #     messages.append(message)
    # await client.delete_messasge(messages)
    # await channel.send('test')


client.run(TOKEN)

