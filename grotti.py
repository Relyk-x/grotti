import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='&')
servername = "ИEVER WΛVE"

@bot.event
async def on_ready():
	print ("------------------------------------")
	print (f"Bot Name: {bot.user.name}")
	print (f"Bot ID: {bot.user.id}")
	print (f"Discord Version: {discord.__version__}")
	print ("Ready to invite new members...")
	print ("------------------------------------")

@bot.command(pass_context=True)
async def invite(ctx, user: discord.Id):
    invite = await bot.say(f"**Invite**\n{user.name} a new server has been partnered! You have been invited to join {servername}\n\n<:discord:535748146761039872> Discord Server: https://discord.gg/SX93MmJ\n")
    await bot.send_message(user, f"{invite}")

bot.run(os.getenv("BOT_TOKEN"))
