import asyncio
import json
import discord
from discord.ext import commands
from mmbot import bot

def add_mail(member_id, channel_id):
	with open('cogs/mail.json', 'r') as f:
		mail = json.load(f)
	mail[channel_id] = member_id
	with open('cogs/mail.json', 'w') as f:
		json.dump(mail, f, indent=4)

def del_mail(channel_id):
	with open('cogs/mail.json', 'r') as f:
		mail = json.load(f)
		mail.pop(str(channel_id))
	with open('mail.json', 'w') as f:
		json.dump(mail, f, indent=4)

async def create_channel(author):
	await author.send('**Please wait untill out staff can reach out to you.**')
	guild = discord.utils.get(bot.guilds, name='you sub to me i sub to you')
	role = discord.utils.get(guild.roles, id=732502832594550785)
	overwrites = {
	guild.default_role: discord.PermissionOverwrite(read_messages=False),
	guild.me: discord.PermissionOverwrite(read_messages=True),
	role: discord.PermissionOverwrite(read_messages=True)
	}
	temp_channel = await guild.create_text_channel(name=author.name.lower(), category=bot.get_channel(778882653104767006))
	add_mail(author.id, temp_channel.id)
	member = await guild.fetch_member(author.id)
	await temp_channel.send("@here Someone wants help.")
	await temp_channel.send(f"**Username:** {author.name}#{author.discriminator} \n**Account Created:** {author.created_at}\n**Joined on:** {member.joined_at}\n**User Id:** {author.id}")
	await temp_channel.send("---------------------------------")
	return temp_channel

class Modmail(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def close(self, ctx, channel: discord.TextChannel = None, *, reason=None):
		channel = channel or ctx.channel
		del_mail(channel.id)
		await channel.delete(reason=reason)

	@close.error
	async def close_error(self, ctx, error):
		if isinstance(error, commands.CheckFailure):
			message = await ctx.send(f"{ctx.author.mention} you need `Manage Channels` permission to use this command")

		else:
			message = await ctx.send(f"{ctx.author.mention} Something Went wrong! Make Sure that I have correct permission and you are running this command in the correct channel.")

		await asyncio.sleep(5)
		await message.delete()

	@commands.command(aliases=['r','reply'])
	async def _send(self, ctx, *, reply=None):
		guild = ctx.guild
		with open('cogs/mail.json','r') as f:
			mail = json.load(f)
		member = await guild.fetch_member(mail[str(ctx.channel.id)])
		await ctx.message.delete()
		await member.send(f"**{ctx.author.name}#{ctx.author.discriminator} :** {reply}")
		await ctx.send(f"**{ctx.author.name} :** {reply}")

	@commands.Cog.listener()
	async def on_message(self, message):
		author = message.author
		if author == bot.user:
			return
		if message.author != message.author.bot:
			if not message.guild:
				channel = discord.utils.get(bot.get_all_channels(), guild__name='you sub to me i sub to you', name=author.name.lower())
				if channel == None:
					channel = await create_channel(author)
				await channel.send(f"**{author.name}#{author.discriminator} :** {message.content}")

def setup(bot):
	bot.add_cog(Modmail(bot))