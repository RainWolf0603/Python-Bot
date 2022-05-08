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
    async def usd(self, ctx, 幣值 : Option(str,"請選擇幣值",choices=["USD", "HKD","EUR","CNY","JPY"]), 金額 : Option(int,"請輸入轉換金額")):
        member = ctx.author
        userAvatar = member.avatar
        if 幣值 == 'USD':
            dollar = 金額 * float(usd[1])
        if 幣值 == 'HKD':
            dollar = 金額 * float(hkd[1])
        if 幣值 == 'EUR':
            dollar = 金額 * float(eur[1])
        if 幣值 == 'CNY':
            dollar = 金額 * float(cny[1])
        if 幣值 == 'JPY':
            dollar = 金額 * float(jpy[1])
        
        embed = discord.Embed(title=(f'台幣轉換{幣值}'), description=(f'{金額}') + f'元{幣值}換算新台幣為:')
        embed.add_field(name='新台幣:', value=(f"{dollar}"), inline=True)
        embed.add_field(name="上次更新時間", value=usd[0], inline=False)
        embed.set_footer(text=('Request by '  + str(member)), icon_url=userAvatar)
        await ctx.respond(embed=embed)

        
def setup(bot):
    bot.add_cog(exchange(bot))