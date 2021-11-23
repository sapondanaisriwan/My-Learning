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

import json
import os
from sys import prefix

import discord
from discord.ext import commands
from dotenv import load_dotenv
from customhelp import CustomHelpCommand

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = get_prefix, help_command = CustomHelpCommand(), intents = intents, case_insensitive=True)

@bot.event
async def on_ready():
    print('Bot is ready')
    if not hasattr(bot, 'appinfo'):
        bot.appinfo = await bot.application_info()
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with you mom"))

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent= 4 )


@commands.has_permissions(administrator=True)
@bot.command(name='prefix', help='Lets you set a new prefix.')
async def change_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent= 4 )


@commands.is_owner()
@bot.command(show_hidden = True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction('👌')


@commands.is_owner()
@bot.command(show_hidden = True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.message.add_reaction('👌')

@commands.is_owner()
@bot.command(show_hidden = True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction('👌')

def main():
    notLoad = ['error handing.py']
    for filename in os.listdir('./cogs'):
        if (filename.endswith('.py')): #and (filename not in notLoad):
            bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    main()    

bot.run(TOKEN)

