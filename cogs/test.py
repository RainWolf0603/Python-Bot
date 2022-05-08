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

    @bot.slash_command(name = "測試2", description = "就說阿")
    async def say(self,ctx,訊息 :Option(str, "輸入要傳的訊息")):
        await ctx.respond(訊息.string.spilit())
        
def setup(bot):
    bot.add_cog(test(bot))