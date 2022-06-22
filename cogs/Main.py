# modules
import random
import json
import os
import discord
import datetime
import time
import math
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

#    @commands.command(aliases=['help'])
#    @commands.cooldown(1, 1, commands.BucketType.user)
#    async def embed(self, ctx, search=None):
#        e = discord.Embed(title='Commands', description='')
#        await ctx.send(embed=e)
    
    # cmds
    @commands.command(aliases=['eta'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def etime(self, ctx, floor:int, damage:int):
        etime = int((floor+3)*round(10/(math.log(damage+1, 10)+1), 0) + 1)
        await ctx.reply(f'Your ETA for Catacombs floor {floor} with {damage} DMG is: {etime}.')
    
    @commands.command(aliases=['ehp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ehealth(self, ctx, hp:int, defense:int):
        v1 = 1 + defense/100
        await ctx.reply(f'Your Effective Health with {hp} HP and {defense} DEF is: {int(hp*v1)}')
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f'Client Latency: {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(MainCog(bot))