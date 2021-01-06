import asyncio
import discord
from discord.ext import commands
from mmbot import bot

class more(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

@commands.command()
async def mtest(self,ctx):
	await ctx.send('is loaded')

def setup(bot):
	bot.add_cog(more(bot))
