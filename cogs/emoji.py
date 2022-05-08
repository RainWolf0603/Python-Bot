import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

def numeric(lol):
    if lol == '1':
        lol = ':one:'
    if lol == '2':
        lol = ':two:'
    if lol == '3':
        lol = ':three:'
    if lol == '4':
        lol = ':four:'
    if lol == '5':
        lol = ':five:'
    if lol == '6':
        lol = ':six:'
    if lol == '7':
        lol = ':seven:'
    if lol == '8':
        lol = ':eight:'
    if lol == '9':
        lol = ':nine:'
    if lol == '0':
        lol = ':zero:'
    return lol

class emoji(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "轉換為表情符號", description = "字面上的意思")
    async def say(self,ctx,字串 : Option(str)):
        字串 = 字串.lower()
        b = list(字串)
        reply = ''
        for char in b:
            if char.isnumeric() == True:
                reply = reply+ numeric(char)
            elif char.isascii() == False or char.isalpha() == False or char.isspace() == True:
                reply = reply + char
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