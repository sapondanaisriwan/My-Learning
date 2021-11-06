import random
from datetime import datetime

import discord
from discord.ext import commands


class Fun_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'Penis size' ,aliases=['pp','ppsize', 'penissize'])
    async def _pennis_size(self, ctx, member: discord.Member):

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


    @commands.command()
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
    bot.add_cog(Fun_Commands(bot))
