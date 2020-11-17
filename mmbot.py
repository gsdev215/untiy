import discord
from itertools import cycle
from discord.ext import commands, tasks
import random
import os
bot = commands.Bot(command_prefix=('.'))

status = cycle(['My Prefix is .', 'Originally I was developed by Dev','My developers username with tag is gs.dev#4082', 'Don\'t try to mess withme and my code','DM me for help | no! don`t dm '])

@bot.event 
async def on_ready():
	change_status.start()
	print('online')
	
	
@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity = discord.Game(next(status)))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def Ping(ctx):
    """Adds two numbers together."""
    await ctx.send(Pong)
    
@bot.command()
async def sub(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
    
@bot.command()
async def mul(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)
    
@bot.command()
async def power(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send((left) ^ right)
    
@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

bot.run(os.environ('TOKEN')
