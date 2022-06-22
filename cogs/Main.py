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

# least values:
# Health: 110
# Defense: 0
# Effective health: 110
# Strength: 1
# Critical Damage: 0
# Intelligence: 110
# Ability Damage: 0
# Estimated damage: 0
# floor: 1

    # cmds
    @commands.command(aliases=['eta'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def etime(self, ctx, floor:int, damage:int):
        if floor < 1 or floor > 7:
            await ctx.reply(f'Catacombs floor {floor} does not exist. Please enter a valid floor number (1-7)')
        else:
            etime = int((floor+3)*round(10/(math.log(damage+1, 10)+1), 0) + 1)
            await ctx.reply(f'Your ETA for Catacombs floor {floor} with {damage} DMG is: {etime}.')
    
    @commands.command(aliases=['ehp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ehealth(self, ctx, hp:int, defense:int):
        if hp < 110 or defense < 0:
            await ctx.reply(f'Please enter a valid Health value (>=110) and a valid Defense value (>=0)')
        else:
            v1 = 1 + defense/100
            await ctx.reply(f'Your Effective Health with {hp} HP and {defense} DEF is: {int(hp*v1)}')

    @commands.command(aliases=['srate'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def survive(self, ctx, floor:int, ehp:int):
        if floor < 0 or floor > 7 or ehp < 110:
            await ctx.reply('Please enter a valid floor number (1-7) and a valid Effective Health value (>=110)')
        elif floor == 1:
            r = ehp/500
        elif floor == 2:
            r = ehp/1000
        elif floor == 3:
            r = ehp/1500
        elif floor == 4:
            r = ehp/3000
        elif floor == 5:
            r = ehp/3500
        elif floor == 6:
            r = ehp/3500
        elif floor == 7:
            r = ehp/10000
        await ctx.reply(f'Your Survival Rate of Catacombs floor {floor} with {ehp} EHP is: {int(r*100)}%')
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f'Client Latency: {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(MainCog(bot))