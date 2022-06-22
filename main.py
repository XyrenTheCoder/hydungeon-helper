# modules
import os
import discord
import datetime
import time
from discord.errors import InvalidArgument
from discord.ext import commands
from discord.ext.commands import *
from keep_alive import keep_alive
# end of modules

bot = commands.Bot(command_prefix=',', intents=discord.Intents.all())
owner = ["thatOneArchUser#5518", "valid-user#0300"]
oid = [706697300872921088, 705462972415213588]
bot.remove_command('help')

# when ready
@bot.event
async def on_ready():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    print(f'\n> {bot.user} HAS CONNECTED TO DISCORD.\n\n')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Hypixel skyblock"))
    print(f'[log] {bot.user} changed its activity.')
# end of startup

@bot.command()
async def load(ctx, *, arg1):
    if ctx.message.author.id in oid:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        print(f"[Cog] {ctx.author} returned an error: User Missing Permission.")
        return
    try:
        bot.load_extension(f'cogs.{arg1}')
        await ctx.send("Loaded Cog")
        print(f"[Cog] {ctx.author} loaded cog.")
        return
    except Exception as e:
        await ctx.send(e)
        print(f"[Cog] An unexpected error has occurred: {e}")

@bot.command()
async def unload(ctx, *, arg1):
    if ctx.message.author.id in oid:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        print(f"[Cog] {ctx.author} returned an error: User Missing Permission.")
        return
    try:
        bot.unload_extension(f'cogs.{arg1}')
        await ctx.send("Unloaded Cog")
        print(f"[Cog] {ctx.author} unloaded cog.")
        return
    except Exception as e:
        await ctx.send(e)
        print(f"[Cog] An unexpected error has occurred: {e}")
        
@bot.command()
async def reload(ctx, *, arg1):
    if ctx.message.author.id in oid:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        print(f"[Cog] {ctx.author} returned an error: User Missing Permission.")
        return
    try:
        bot.unload_extension(f'cogs.{arg1}')
        bot.load_extension(f'cogs.{arg1}')
        await ctx.send("Reloaded Cog")
        print(f"[log] {ctx.author} reloaded cog.")
        return
    except Exception as e:
        await ctx.send(e)
        print(f"[Cog] An unexpected error has occurred: {e}")

bot.load_extension("cogs.MainCog")
bot.load_extension("cogs.ErrorHandler")
keep_alive()
bot.run('token')



# btw i use arch
