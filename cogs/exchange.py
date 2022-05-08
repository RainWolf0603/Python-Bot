import discord
from discord.ext import commands as cmds
from discord.commands import Option
import twder

usd = float(twder.now('USD')[1])
hkd = float(twder.now('HKD')[1])
eur = float(twder.now('EUR')[1])
cny = float(twder.now('CNY')[1])
jpy = float(twder.now('JPY')[1])

bot = discord.Bot()

class exchange(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "匯率轉換", description = "換錢")
    async def usd(self, ctx, 幣值 : Option(str,"請選擇幣值",choices=["USD", "HKD","EUR","CNY","JPY"]), 金額 : Option(int,"請輸入轉換金額")):
        member = ctx.author
        userAvatar = member.avatar
        if 幣值 == 'USD':
            bruh = 金額 * float(usd[1])
        embed = discord.Embed(title=(f'台幣轉換{幣值}'), description=(f'{金額}') + f'元{幣值}換算新台幣為:{bruh}')
        embed.add_field(name='新台幣:', value=(str(twder.now(f'{幣值}')[1])), inline=True)
        embed.add_field(name="上次更新時間", value=usd[0], inline=False)
        embed.set_footer(text=('Request by '  + str(member)), icon_url=userAvatar)
        await ctx.respond(embed=embed)

        


def setup(bot):
    bot.add_cog(exchange(bot))
