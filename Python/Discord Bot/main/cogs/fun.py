import random
from datetime import datetime

import discord
from discord.ext import commands


class FunCommand(commands.Cog, name='Fun commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(name= 'ppsize' ,aliases=['pp', 'penissize'], help='คำนวณขนาดหำของผู้ใช้')
    async def pennis_size(self, ctx, member: discord.Member):

        if member.bot or ctx.author.bot:
            return

        pp_size = ['เล็กชิบหาย 🤏', 'เล็กชิบหาย 🤏', 'เล็กชิบหาย 🤏', 'เล็กชิบหาย 🤏', 'ปานกลาง 🙄', 'ปานกลาง 🙄',  'ใหญ่ 💪','โคตรใหญ่ 😱']

        embed = discord.Embed(
            title = 'ระบบคำนวณขนาดหำ',
            description=f'{member.mention} หำ{random.choice(pp_size)}'
        )
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text = f"ID - {member.avatar}")

        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help='คำนวณความเป็นเกย์ของผู้ใช้')
    async def gay(self, ctx, member: discord.Member):

        if member.bot or ctx.author.bot:
            return

        embed = discord.Embed(
            title = 'ระบบคำนวณความเป็นเกย์',
            description=f'{member.mention} เป็นเกย์ `{random.randint(0, 100 + 1)}%`'
        )
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text = f"ID - {member.avatar}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunCommand(bot))
