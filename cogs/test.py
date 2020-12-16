import discord
from discord.ext import commands
import datetime

import os
import random
from dotenv import load_dotenv
import youtube_dl
import math
import random
import youtube_dl

bot = commands.Bot(command_prefix=('.'))
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available.')
    embed.add_field(name=',ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name=',info', value='Random info stuff', inline=False)
	await ctx.send(embed=embed)
