from optparse import Option
import discord
from discord.ext import commands as cmds
from discord.commands import Option


class purge(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = discord.Bot()

    @bot.slash_command(name = "刪除", description = "刪除數量")
    async def purge(self, ctx, 數量: Option(int, "輸入要刪除訊息的數量")):
        await ctx.channel.purge(limit=數量)
        await ctx.respond(f"已刪除 {數量} 則訊息")

def setup(bot):
    bot.add_cog(purge(bot))