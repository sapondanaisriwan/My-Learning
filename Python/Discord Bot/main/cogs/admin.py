from datetime import datetime
import discord
from discord.ext import commands


class AdminCommand(commands.Cog, name='Admin commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        channel = self.bot.get_channel(912001523016400936)

        if message.author.bot:
            return

        embed = discord.Embed(
            title=f"Message Deleted",
            description=f"**User:** <@{message.author.id}>\n"
            f"**Message:** \n{message.content}",
            color=0xbf0404,
        )
        embed.set_author(name=f"{message.author}",
                         icon_url=f"{message.author.display_avatar}")
        for attachment in message.attachments:
            if 'image' in attachment.content_type:
                embed.set_image(url=attachment.proxy_url)
            else:
                embed.description += f"{attachment.proxy_url}"

        await channel.send(embed=embed)

    @commands.command(help="Change member's name that you mention")
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, nickname):

        if ctx.author.bot:
            return

        embed = discord.Embed(
            description=f'Nickname was changed to {member.mention}.'
        )

        await member.edit(nick=nickname)
        await ctx.send(embed=embed)

    @commands.command(name='resetnick', aliases=['rsnick'], help="Resets member's name that you mention")
    @commands.has_permissions(manage_nicknames=True)
    async def reset_nick(self, ctx, member: discord.Member):

        if ctx.author.bot:
            return

        embed = discord.Embed(
            description=f'Nickname was reset to {member.mention}.'
        )

        await member.edit(nick=None)
        await ctx.send(embed=embed)

    @commands.command(help='Kicks the user you specified out of your server.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        if ctx.author.bot:
            return

        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kick')

    @commands.command(help='Bans the user you specified out of your server.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):

        if ctx.author.bot:
            return

        await member.ban(reason=reason)
        await ctx.send(f'User {member.mention} has been banned')

    @commands.command(help='Unbans the user you provided from in this server')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):

        if ctx.author.bot:
            return

        # [BanEntry(reason='fuck you', user=<User id=554181520286547999 name='Katozai' discriminator='5852' bot=False>)]
        banned_users = await ctx.guild.bans()  # get all the user who has gotten banned
        member_name = member_discriminator = member_id = None

        try:
            member_name, member_discriminator = member.split(
                '#')  # member_discriminator = user's tag
        except:
            member_id = member

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator) or (user.id == int(member_id)):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


def setup(bot):
    bot.add_cog(AdminCommand(bot))
