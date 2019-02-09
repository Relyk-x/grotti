import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import datetime
from datetime import datetime
import time
import bs4, requests
import os

bot = commands.Bot(command_prefix='v!')
servername = "ИEVER WΛVE"
@bot.event
async def on_ready():
	servers = list(bot.servers)
#status = f"over {str(len(bot.servers))} servers"
	status = f"for {pref}commands"
	print ("------------------------------------")
	print (f"Bot Name: {bot.user.name}")
	print (f"Bot ID: {bot.user.id}")
	print (f"Discord Version: {discord.__version__}")
	print ("Ready to invite new members...")
	print ("------------------------------------")
	await bot.change_presence(game=discord.Game(name=status,type=3))

@bot.command(pass_context=True)
async def invite(ctx, user: user.id):
    invite = await bot.say(f"**Invite**\n{user.name} you have been invited to join {servername}\n\n**Link**\n<:discord:535748146761039872> Discord Server: https://discord.gg/SX93MmJ\n")
    await bot.send_message(ctx.message.user.id, f"{invite}")

    discord.Embed(title="Invite", description = f"{user.name} you have been invited to join {servername}", color=0x7289da,)
    embed.add_field(name="Link", value="<:discord:535748146761039872> Discord Server: https://discord.gg/SX93MmJ")
    await bot.send_message(ctx.message.user.id, embed=embed)

bot.run(os.getenv("BOT_TOKEN"))
