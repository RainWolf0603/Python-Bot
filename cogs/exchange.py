import discord
from discord.ext import commands as cmds
from discord.commands import Option
import twder

usd = twder.now('USD')
hkd = twder.now('HKD')
eur = twder.now('EUR')
cny = twder.now('CNY')
jpy = twder.now('JPY')

bot = discord.Bot()

class exchange(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "匯率轉換", description = "換錢")
    async def usd(self, ctx, 幣值 : Option(str,"請選擇幣值",choices=["美金", "港幣","歐元","人民幣","日幣"]), 金額 : Option(int,"請輸入轉換金額")):
        member = ctx.author
        userAvatar = member.avatar
        await ctx.respond(f'台幣轉換{幣值}結果如下')
        embed = discord.Embed(title=(f'台幣轉換{幣值}'), description=(f'{金額}') + f'元{幣值}金換算新台幣為:')
        #放在下面才if是因為上面的{幣值}才會變成中文
        if 幣值 == "美金": 幣值 = "USD"
        if 幣值 == "港幣": 幣值 = "HKD"
        if 幣值 == "歐元": 幣值 = "EUR"
        if 幣值 == "人民幣": 幣值 = "CNY"
        if 幣值 == "日幣": 幣值 = "JPY"
        embed.add_field(name='新台幣:', value=(str(twder.now(f'{幣值}')[1])), inline=True)
        embed.add_field(name="上次更新時間", value=usd[0], inline=False)
        embed.set_footer(text=('Request by '  + str(member)), icon_url=userAvatar)
        await ctx.send(embed=embed)

        


def setup(bot):
    bot.add_cog(exchange(bot))