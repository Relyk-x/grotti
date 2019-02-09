import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print ("------------------------------------")
    print (f"Bot Name: {bot.user.name}")
    print (f"Bot ID: {bot.user.id}")
    print (f"Discord Version: {discord.__version__}")
    print ("Ready to invite new members...")
    print ("------------------------------------")

#@bot.command(pass_context=True)
#async def invite(ctx, user: discord.Member):
    #partner = f"**Invite**\n{user.name} a new server has been partnered! You have been invited to join {servername}\n\n<:discord:535748146761039872> Discord Server: https://discord.gg/8GNRBsr"
    #await bot.send_message(user, f"{partner}")

@bot.command(pass_context = True)
async def member_id(ctx):
    memb = list(bot.members)
    for x in range(len(memb)):
        await bot.say("memb[x-1].id")


@bot.command(pass_context = True)
async def invite(ctx, userToInvite):
    inviteLinq = await bot.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 1)
    target_user = await bot.get_user_info(userToInvite)
    await bot.send_message(target_user, f"**Invite**\nA new server has been partnered! You are invited to join...\n{inviteLinq}")

bot.run(os.getenv("BOT_TOKEN"))
