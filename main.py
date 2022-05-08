import discord
import json
import os
import pathlib
from discord.ext import commands as cmds

bot = discord.Bot(activity = discord.Activity(type=discord.ActivityType.watching, name="好了啦特哥椅子哥丹利哥死哥維爾戈靈魂收割多佛朗明哥豬大哥蒼藍鴿中華民國國歌UC姐K7姐好運姐冰冰姐美鳳姐小燕姐法拉利姐曾聖傑林俊傑傳奇羅傑端午節中秋節"))

Path = pathlib.Path().absolute()

with open(fr'{Path}/config.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

@bot.event
async def on_ready():
    print('{0.user} wake the fuck up'.format(bot))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        

@bot.slash_command(name = "reload", description = "reload")
@cmds.has_permissions(administrator = True)
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')
            bot.load_extension(f'cogs.{filename[:-3]}')
    await ctx.respond('✅')



bot.run(jdata['token'])
