import discord
from dotenv import load_dotenv
from itertools import cycle
from discord.ext import commands
import random
import time
import os
from mmbot import bot


class Fun(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

@commands.command()
async def say (ctx, arg):
    await ctx.send(arg)

@commands.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
