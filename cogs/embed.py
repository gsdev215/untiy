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
