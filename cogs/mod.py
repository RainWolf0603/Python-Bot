import discord
from datetime import datetime
from discord import Option
from discord.ext import commands as cmds
from discord.ext.commands import MissingPermissions

bot = discord.Bot()

class mod(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot
    
@bot.slash_command(name = "bans", description = "Get a list of members who are banned from this server!")
@cmds.has_permissions(ban_members = True)
async def bans(ctx):
    await ctx.defer()
    bans = await ctx.guild.bans()
    embed = discord.Embed(title = f"List of Bans in {ctx.guild}", timestamp = datetime.now(), color = discord.Colour.red())
    for entry in bans:
        if len(embed.fields) >= 25:
            break
        if len(embed) > 5900:
            embed.add_field(name = "Too many bans to list")
        else:
            embed.add_field(name = f"Ban", value = f"Username: {entry.user.name}#{entry.user.discriminator}\nReason: {entry.reason}\nUser ID: {entry.user.id}\nIs Bot: {entry.user.bot}", inline = False)
    await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(mod(bot))