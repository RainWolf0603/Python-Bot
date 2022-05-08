import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class announce(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "公告", description = "公告訊息")
    async def say(self,ctx,公告 :Option(str, "輸入要公告的訊息"),提及 :Option(str,"要不要標註",choices=["@everyone", "@here","不要提及"])):
        member = ctx.author
        userAvatar = member.avatar
        if 提及 == "@everyone" : await ctx.respond("@everyone")
        elif 提及 == "@here" : await ctx.respond("@here")
        else : None
        embed = discord.Embed(title=('公告'), description=(f'{公告}'))
        embed.set_footer(text=('發布者 '  + str(member)), icon_url=userAvatar)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(announce(bot))