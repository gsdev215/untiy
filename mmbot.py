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

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Test")
    await client.add_roles(user, role)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(788709479897104384)
    embed = discord.Embed(title="Welcome :-", description="Thank you for kindly joining our server", color=0x00ff00)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    embed.add_field(name="IP" , value="play.unitypixel.net", inline=True) 
    embed.add_field(name="Port", value="19132", inline=True) 
    embed.set_footer(text="Hope u stay here longer")
    await channel.send(content=f"{member.mention}",embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(788709479897104384)
    embed = discord.Embed(title="Good Bye :-", description="Thank you for being with us hope to see you soon.", color=0x00ff00)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    await member.send(embed=embed)
    await channel.send(embed=embed)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(os.getenv('TOKEN'))
