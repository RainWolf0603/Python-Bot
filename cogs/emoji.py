import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class emoji(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "轉換為表情符號", description = "字面上的意思")
    async def say(self,ctx,字串 : Option(str)):
        字串 = 字串.lower()
        b = list(字串)
        reply = ''
        for char in b:
            if char.isspace() == True:
                reply = reply + char
            elif char.isascii() == False:
                reply = reply+char
            else:
                reply= reply + ':regional_indicator_' + char + ':'
        await ctx.respond(reply)

    @bot.slash_command(name = "表情符號階梯", description = "字面上的意思")
    async def xd(self,ctx,字串 : Option(str)):
        字串 = 字串.lower()
        b = list(字串)
        reply = ''
        for char in b:
            if char.isspace() == True:
                reply = reply + char
            elif char.isascii() == False:
                reply = reply+char
            else:
                reply= reply + ':regional_indicator_' + char + ':'
                await ctx.respond(reply)

def setup(bot):
    bot.add_cog(emoji(bot))