import discord

from io import BytesIO
from utils import default
from dotenv import load_dotenv
from itertools import cycle
from discord.ext import commands
import random
import time
import os

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

@commands.command()
@commands.guild_only()
async def say (ctx, arg):
    await ctx.send(arg)

@commands.command()
@commands.guild_only()
async def slap(ctx, member: discord.Member, *, reason=''):
    await ctx.send(f'{member.name} just got slapped from {ctx.author.name} for {reason}') 
 

def setup(bot):
	bot.add_cog(command(bot))
