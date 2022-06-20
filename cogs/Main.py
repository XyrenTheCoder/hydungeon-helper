# modules
import random
import json
import os
import discord
import datetime
import time
import math
import string
from datetime import datetime
from discord.errors import InvalidArgument
from discord.ext import commands
from discord.ext.commands import *
# end of modules

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def embed(self, ctx, search=None): ...
    
    # cmds
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roll(self, ctx): ...
    
    @commands.command(aliases=[''])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def q(self, ctx): ...
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f'Client Latency: {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(MainCog(bot))
