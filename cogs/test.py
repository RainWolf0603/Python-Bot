import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class test(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "測試", description = "測試")
    async def say(self,ctx,選擇 : Option(str,choices=["1", "2","3"])):
      await ctx.respond(f'{選擇}')
        
def setup(bot):
    bot.add_cog(test(bot))