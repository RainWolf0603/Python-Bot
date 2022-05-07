from optparse import Option
import discord
from discord.ext import commands as cmds
from discord.commands import Option

bot = discord.Bot()

class resistance(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "電阻顏色到數量", description = "測試")
    async def resistance(self,ctx,
    顏色一 : Option(str,choices=["黑", "棕","紅","橙","黃","綠","藍","紫","灰","白"]),
    顏色二 : Option(str,choices=["黑", "棕","紅","橙","黃","綠","藍","紫","灰","白"]),
    顏色三 : Option(str,choices=["黑", "棕","紅","橙","黃","綠","藍","紫","灰","白","金","銀"]),
    顏色四 : Option(str,choices=["棕", "紅","綠","藍","紫","灰","金","銀","無"]),):
    #顏色一
        if 顏色一 == "黑": 顏色一 = "0"
        if 顏色一 == "棕": 顏色一 = "1"
        if 顏色一 == "紅": 顏色一 = "2"
        if 顏色一 == "橙": 顏色一 = "3"
        if 顏色一 == "黃": 顏色一 = "4"
        if 顏色一 == "綠": 顏色一 = "5"
        if 顏色一 == "藍": 顏色一 = "6"
        if 顏色一 == "紫": 顏色一 = "7"
        if 顏色一 == "灰": 顏色一 = "8"
        if 顏色一 == "白": 顏色一 = "9"
    #顏色二
        if 顏色二 == "黑": 顏色二 = "0"
        if 顏色二 == "棕": 顏色二 = "1"
        if 顏色二 == "紅": 顏色二 = "2"
        if 顏色二 == "橙": 顏色二 = "3"
        if 顏色二 == "黃": 顏色二 = "4"
        if 顏色二 == "綠": 顏色二 = "5"
        if 顏色二 == "藍": 顏色二 = "6"
        if 顏色二 == "紫": 顏色二 = "7"
        if 顏色二 == "灰": 顏色二 = "8"
        if 顏色二 == "白": 顏色二 = "9"
    #顏色三
        if 顏色三 == "黑": 顏色三 = (str(int(float(f'{顏色一}{顏色二}')*1)))                                    #1
        if 顏色三 == "棕": 顏色三 = (str(int(float(f'{顏色一}{顏色二}')*10)))                                 #10
        if 顏色三 == "紅": 顏色三 = (str(round(float(f'{顏色一}{顏色二}')*0.1,1)) + 'K')           #0.1K
        if 顏色三 == "橙": 顏色三 = (f'{顏色一}{顏色二}') + "K"                                                              #1K
        if 顏色三 == "黃": 顏色三 = (str(int(float(f'{顏色一}{顏色二}')*10)) + 'K')                        #10K
        if 顏色三 == "綠": 顏色三 = (str(round(float(f'{顏色一}{顏色二}')*0.1,1)) + 'M')           #0.1M
        if 顏色三 == "藍": 顏色三 = (f'{顏色一}{顏色二}') + "M"                                                              #1M
        if 顏色三 == "紫": 顏色三 = (str(int(float(f'{顏色一}{顏色二}')*10)) + 'M')                        #10M
        if 顏色三 == "灰": 顏色三 = (str(int(float(f'{顏色一}{顏色二}')*100)) + 'M')                     #100M
        if 顏色三 == "白": 顏色三 = (str(int(float(f'{顏色一}{顏色二}')*1)) + 'G')                            #1G
        if 顏色三 == "金": 顏色三 = (str(round(float(f'{顏色一}{顏色二}')*0.1,1)))                       #0.1
        if 顏色三 == "銀": 顏色三 = (str(round(float(f'{顏色一}{顏色二}')*0.01,1)))                    #0.01
    #顏色四
        if 顏色四 == "棕": 顏色四 = "± 1%"
        if 顏色四 == "紅": 顏色四 = "± 2%"
        if 顏色四 == "綠": 顏色四 = "± 0.5%"
        if 顏色四 == "藍": 顏色四 = "± 0.25%"
        if 顏色四 == "紫": 顏色四 = "± 0.1%"
        if 顏色四 == "灰": 顏色四 = "± 0.05%"
        if 顏色四 == "金": 顏色四 = "± 5%"
        if 顏色四 == "銀": 顏色四 = "± 10%"
        if 顏色四 == "無": 顏色四 = "± 20%"


        await ctx.respond('你選擇了' + f'{顏色三}' + f'{顏色四}')
        

def setup(bot):
    bot.add_cog(resistance(bot))