import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class invite(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "邀請", description = "邀請機器人")
    async def say(self,ctx,機器人 :Option(str, "輸入要邀請的機器人ID"),斜線指令: Option(str,"要開啟斜線指令嗎 ",choices=["是", "否"])):
        if 斜線指令 == "是": 斜線指令 = "%20applications.commands"
        if 斜線指令 == "否": 斜線指令 = ""
        await ctx.respond(f'https://discord.com/api/oauth2/authorize?client_id={機器人}&permissions=8&scope=bot{斜線指令}')
def setup(bot):
    bot.add_cog(invite(bot))