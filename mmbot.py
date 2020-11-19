import discord
from dotenv import load_dotenv
from itertools import cycle
from discord.ext import commands, tasks
import random
import time
import os

load_dotenv()

bot = commands.Bot(command_prefix=('.'))
bot.remove_command('help')

status = cycle(['My Prefix is .', 'Originally I was developed by Dev','My developers username with tag is gs.dev#4082', 'Don\'t try to mess withme and my code','DM me for help | no! don`t dm '])

@bot.event 
async def on_ready():
	change_status.start()
	print(f'Logged in as {bot.user.name}')
	
	
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity = discord.Game(next(status)))
    
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    before_ws = int(round(bot.latency * 1000, 1))
    message = await ctx.send("🏓 Pong")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(os.getenv('TOKEN'))
