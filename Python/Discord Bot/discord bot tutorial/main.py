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

intents = discord.Intents.all()
PREFIX = "!!"
bot = commands.Bot(command_prefix=PREFIX, intents=intents, )


"""
Catch error message
"""

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing a required argument.")

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to run this command.")
    
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have sufficient permissions!")


"""
bot EVENT
"""

@bot.event
async def on_ready():
    print('Bot is ready')


@bot.event
async def on_message(message):

    if message.author.bot:
        return
    
    await bot.process_commands(message)
    

# detect deleted message
@bot.event
async def on_message_delete(message):

    if message.author.bot:
        return

    if message.content: # to ignore the error if user send an image
        await message.channel.send(message.content)


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@bot.command()
async def clear(ctx, amount=5):

    if ctx.author.bot:
        return

    await ctx.channel.purge(limit = amount + 1)


@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'User {member} has been kick')


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned')


bot.run(TOKEN)

