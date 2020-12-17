import discord
from dotenv import load_dotenv
from itertools import cycle
from discord.ext import commands, tasks
import random
import time
import os

load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=('.'), intents=intents)
bot.remove_command('help')

@bot.commands
async def say (ctx, arg):
    await ctx.send(arg)

@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
