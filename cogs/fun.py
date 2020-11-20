import asyncio
import discord
from discord.ext import commands
from mmbot import bot

class Fun(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def math(self, ctx, *,expression=""):
		try:
			await ctx.send(f"**The answer of your expression is:** {eval(expression)}")
		except Exception:
			temp_msg = await ctx.send("Please provide a valid expression.")
			await asyncio.sleep(5)
			await temp_msg.delete()

def setup(bot):
	bot.add_cog(Fun(bot))