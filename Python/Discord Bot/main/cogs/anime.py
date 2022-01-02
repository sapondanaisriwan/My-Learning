import discord
import json
import re
import web_scrapping
from discord.ext import commands, tasks


class Anime(commands.Cog, name='Anime notification'):
    def __init__(self, bot):
        self.bot = bot
        self.update_anime_list.start()

    @tasks.loop(hours=1)
    async def update_anime_list(self):
        await web_scrapping.main()
        print('List has been updated')

    @commands.command(name='anime', help="Update anime list")
    async def display_anime(self, ctx):
        with open('clean_data.json', 'r', encoding='utf-8') as f:
            data = f.read()
            toJson = json.loads(data)
        embed = discord.Embed(
            title = f"**Anime Updated**"
            # description = f"**Just Updated**",
        )
        print('here')
        animeQueue = 1
        for v in toJson:
            if v['status'].startswith('อัปเดต'):
                newEP = " New EP:" + str(int(re.search(r'\d+', v['status']).group()))
                embed.description += f"\n{animeQueue}). [{v['title'] + newEP}]({v['url']})"
                animeQueue += 1
                # embed.description += f"{v['status']}"
        await ctx.send(embed=embed)
        # for i in range(len(toJson[0])):
        #     await ctx.send(string)


def setup(bot):
    bot.add_cog(Anime(bot))
