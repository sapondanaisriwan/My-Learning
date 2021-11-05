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
import random
from datetime import datetime
from discord import embeds
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
PREFIX = "!!"
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
    await ctx.send(f'User {member.mention} has been banned')


@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):

    # [BanEntry(reason='fuck you', user=<User id=554181520286547999 name='Katozai' discriminator='5852' bot=False>)]
    banned_users = await ctx.guild.bans() # get all the user who has gotten banned
    member_name = member_discriminator = member_id = None

    try:
        member_name, member_discriminator = member.split('#') # member_discriminator = user's tag
    except:
        member_id = member

    for ban_entry  in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator) or (user.id == int(member_id)):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@bot.command()
@commands.has_permissions(manage_nicknames = True)
async def nick(ctx, member: discord.Member, *, nickname):

    embed = discord.Embed(
        description=f'Nickname was changed to {member.mention}.'
    )

    await member.edit(nick = nickname)
    await ctx.send(embed=embed)


@bot.command(aliases=['reset', 'rsnick', 'resetnick'])
@commands.has_permissions(manage_nicknames = True)
async def reset_nick(ctx, member: discord.Member):

    embed = discord.Embed(
        description=f'Nickname was reset to {member.mention}.'
    )

    await member.edit(nick = None)
    await ctx.send(embed=embed)


@bot.command(aliases=['pp','ppsize', 'penissize'])
async def _pennis_size(ctx, member: discord.Member):

    if member.bot or ctx.author.bot:
        return

    pp_size = ['เล็กชิบหาย 🤏', 'เล็กชิบหาย 🤏', 'เล็กชิบหาย 🤏', 'เล็กชิบหาย 🤏', 'ปานกลาง 🙄', 'ปานกลาง 🙄',  'ใหญ่ 💪','โคตรใหญ่ 😱']
    date = datetime.now().strftime("%x") # บอกวันเวลา

    embed = discord.Embed(
        title = 'ระบบคำนวณขนาดหำ',
        description=f'{member.mention} หำ{random.choice(pp_size)}'
    )

    embed.set_footer(text = f"ID - {member.avatar} • {date}")
    await ctx.send(embed=embed)


@bot.command()
async def gay(ctx, member: discord.Member):

    if member.bot or ctx.author.bot:
        return

    date = datetime.now().strftime("%x") # บอกวันเวลา

    embed = discord.Embed(
        title = 'ระบบคำนวณความเป็นเกย์',
        description=f'{member.mention} เป็นเกย์ `{random.randint(0, 100)}%`'
    )

    embed.set_footer(text = f"ID - {member.avatar} • {date}")
    await ctx.send(embed=embed)

bot.run(TOKEN)

