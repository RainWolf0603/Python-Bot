import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class say(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "說", description = "就說阿")
    async def say(self,ctx,訊息 :Option(str, "輸入要傳的訊息")):
      await ctx.respond(f'{訊息}')

def setup(bot):
    bot.add_cog(say(bot))