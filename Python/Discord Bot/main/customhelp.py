import discord
import json
from discord.ext import commands
from datetime import datetime


class CustomHelpCommand(commands.MinimalHelpCommand):

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        ctx = self.context
        destination = self.get_destination()
        with open('prefixes.json', 'r') as f:
            prefix = json.load(f)
        embed = discord.Embed(
            color=0x30e8ba,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=f"| Command lists",
            icon_url=ctx.author.display_avatar
        )
        embed.set_footer(
            text=f"Use `{prefix[str(ctx.guild.id)]}help <CommandName>` to get more information about a command.",
        )
        for cog in mapping:
            if cog != None:
                All_Commands = ', '.join(
                    [f'`{command.name}`' for command in mapping[cog]])
                if len(All_Commands) > 0:
                    embed.add_field(
                        name=f'{cog.qualified_name} ({(len(mapping[cog]))})',
                        value=All_Commands,
                        inline=False
                    )

        await destination.send(embed=embed)

    async def send_cog_help(self, cog):
        print(cog)
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        ctx = self.context
        print(dir(ctx))
        alias = command.aliases
        destination = self.get_destination()

        embed = discord.Embed(
            title=command.name,
            description=command.help,
            timestamp=datetime.utcnow()
        )
        embed.add_field(
            name="• Usage",
            value=f'`{self.get_command_signature(command).lower()}`'
        )
        embed.set_footer(
            text=f'Request By: {ctx.author}',
            icon_url=ctx.author
        )

        if alias:
            embed.add_field(
                name="• Aliases",
                value=", ".join([f'`{aliases}`' for aliases in alias]),
                inline=False
            )
        await destination.send(embed=embed)

    async def send_error_message(self, error):
        pass
        # embed = discord.Embed(title="Error", description=error)
        # channel = self.get_destination()
        # await channel.send(embed=embed)
