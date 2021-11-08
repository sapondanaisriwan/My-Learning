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
from datetime import datetime
from sys import prefix

import discord
from discord.ext import commands
from dotenv import load_dotenv

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

class CustomHelpCommand(commands.MinimalHelpCommand):
    def __init__(self):
        super().__init__()  

    async def send_bot_help(self, mapping):
        ctx = self.context
        destination = self.get_destination()
        with open('prefixes.json', 'r') as f: prefix = json.load(f)
        embed = discord.Embed(
            color = 0x30e8ba,
            timestamp = datetime.utcnow()
        )
        embed.set_author(
            name = f"| Command lists",
            icon_url = ctx.author.avatar_url
        )
        embed.set_footer(   
            text = f"Use `{prefix[str(ctx.guild.id)]}help <CommandName>` to get more information about a command.",
        )
        for cog in mapping:
            if cog != None:
                All_Commands = ', '.join([f'`{command.name}`' for command in mapping[cog]])
                embed.add_field(
                    name = f'{cog.qualified_name} ({(len(mapping[cog]))})',
                    value = All_Commands,
                    inline = False
                )

        await destination.send(embed=embed)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)
    
    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        ctx = self.context
        alias = command.aliases
        destination = self.get_destination()

        embed = discord.Embed(
            title = command.name,
            description = command.help,
            timestamp = datetime.utcnow()
        )
        embed.add_field(
            name="• Usage", 
            value = f'`{self.get_command_signature(command).lower()}`'
        )
        embed.set_footer(
            text = f'Request By: {ctx.author}',
            icon_url = ctx.author.avatar_url
        )

        if alias:
            embed.add_field(
                name="• Aliases",
                value=", ".join([f'`{aliases}`' for aliases in alias]),
                inline=False
            )
        await destination.send(embed=embed)

    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error)
        channel = self.get_destination()
        await channel.send(embed=embed)
    
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = get_prefix, help_command = CustomHelpCommand(), intents = intents)

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
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    main()


bot.run(TOKEN)

