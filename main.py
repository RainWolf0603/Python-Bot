import discord
from discord.ext import commands as cmds
import os

token = "OTcyMDU2OTUzNjE2NDk0NjEy.YnTglQ.pOQQoSkl7pTr-nw_VdtswGyEzjA"

bot = discord.Bot(command_prefix='=')


@bot.event
async def on_ready():
    print('{0.user} wake the fuck up'.format(bot))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        

@bot.slash_command(name = "reload", description = "reload")
async def reload(ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
                bot.load_extension(f'cogs.{filename[:-3]}')
            await ctx.respond(f'{filename} Reloaded')

bot.run(token)