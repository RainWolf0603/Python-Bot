import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class math(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "運算", description = "簡單數學運算")
    async def say(self,ctx,
    數字1 :Option(float, "數字1"),
    數字2 :Option(float,"數字2"),
    計算 : Option(str,choices=["加", "減","乘","除","整數除法","取餘數","次方"])):
        if 計算 == "加": 計算 = (數字1 + 數字2)
        if 計算 == "減": 計算 = (數字1 - 數字2)
        if 計算 == "乘": 計算 = (數字1 * 數字2)
        if 計算 == "除": 計算 = (數字1 / 數字2)
        if 計算 == "整數除法": 計算 = (數字1 // 數字2)
        if 計算 == "取餘數": 計算 = (數字1 % 數字2)
        if 計算 == "次方": 計算 = (數字1 ** 數字2)
        await ctx.respond(計算)

def setup(bot):
    bot.add_cog(math(bot))