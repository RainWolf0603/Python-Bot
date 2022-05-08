import discord
import json
import os
import pathlib
from discord.ext import commands as cmds
bot = discord.Bot()
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
