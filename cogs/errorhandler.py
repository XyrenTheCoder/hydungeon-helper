# modules
import os
import discord
import datetime
import time
from datetime import datetime
from discord.errors import InvalidArgument
from discord.ext import commands
from discord.ext.commands import *
# end of modules

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)
        if isinstance(error, ignored):
            return
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing required argument(s).')
            print(f'[log] {ctx.author} returned an error: {error}.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have the permission to do that. :eyes:")
            print(f'[log] {ctx.author} returned an error: {error}.')
        if isinstance(error, BotMissingPermissions):
            await ctx.send('I don\'t have the required permissions to use this.')
            print(f'[log] {ctx.author} returned an error: {error}.')
        if isinstance(error, BadArgument):
            await ctx.send('Invalid argument')
            print(f'[log] {ctx.author} returned an error: {error}.')
        if isinstance(error, commands.CommandOnCooldown):
            if math.ceil(error.retry_after) < 60:
                await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(error.retry_after)} seconds')
                print(f'[log] {ctx.author} returned an error: {error}.')
            elif math.ceil(error.retry_after) < 3600:
                ret = math.ceil(error.retry_after) / 60
                await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)} minutes')
                print(f'[log] {ctx.author} returned an error: {error}.')
            elif math.ceil(error.retry_after) >= 3600:
                ret = math.ceil(error.retry_after) / 3600
                if ret >= 24:
                    r = math.ceil(ret) / 24
                    await ctx.reply(f"This command is on cooldown. Please try after {r} days")
                    print(f'[log] {ctx.author} returned an error: {error}.')
                else:
                    await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)}')
                    print(f'[log] {ctx.author} returned an error: {error}.')
                # How to use cooldowns:
                # after @commands.command() add @commands.cooldown(1, cooldown, commands.BucketType.user)

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
