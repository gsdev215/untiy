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
#bot.remove_command('help')



status = cycle(['My Prefix is .', 'Originally I was developed by Dev','My developers username with tag is gs.dev#4082', 'Don\'t try to mess withme and my code','DM me for help | no! don`t dm '])

@bot.event 
async def on_ready():
	change_status.start()
	print(f"Logged in as {bot.user.name}")
	
	
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity = discord.Game(next(status)))
    

@bot.command()
async def load(ctx , extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))

@bot.command()
async def ping(ctx):
    before = time.monotonic()
    before_ws = int(round(bot.latency * 1000, 1))
    message = await ctx.send("🏓 Pong")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(member):
    user = member.message.author
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

'''@bot.command()
async def help (member):
    embed=discord.Embed(title="HELP", description="here are the commands that i can execute right at this moment. ", color=0x0666fd)
    embed.add_field(name=".help", value="the command you must just now", inline=True)
    embed.add_field(name=".math", value="now you can slove your math problem.  just type .math (value1)(operation :- , - , + , * , **, /,^) (value2)", inline=True)
    embed.add_field(name=".mods", value="now u can check how all are mod and there status(online|ideal|dnd) . cool right", inline=True)
    embed.add_field(name=".server", value="gives info about the server ", inline=True)
    embed.add_field(name=".user /.user (tag a person, eg :- @NASAfounder)", value="gives details about that person", inline=True)
    embed.add_field(name=".server avatar", value="full zoomed server icon", inline=True)
    embed.add_field(name=".joindat /.joindat (tag a person)", value="show that person join date both discord and this server.", inline=True)
    embed.set_footer(text="bot by :- gs.dev#0428")
    await member.send(embed=embed)'''

@bot.command()
async def ip (ctx):
    embed=discord.Embed(title="IP", color=0x2cdedb)
    embed.add_field(name="JAVA IP", value="play.unitypixel.net", inline=False)
    embed.add_field(name="Bedrock IP", value="play.unitypixel.net", inline=True)
    embed.add_field(name="port", value="19132", inline=True)
    await ctx.send(embed=embed)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        name = filename[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(os.getenv('TOKEN'))
