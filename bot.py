# bot.py
import discord
from dotenv import load_dotenv
import os
from leetcode_requests import get_leetcode_daily

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

GENERAL_CHANNEL = 1007826049347891201
LEETCODE_CHANNEL = 1008072276396216342

@bot.event # registers event
async def on_ready(): # once bot is online
    print(f'{bot.user} connected to Discord!')

# @bot.event
# async def on_message(message): # on receiving a message
#     if message.author == bot.user: # doesn't do anything is message is from bot
#         return

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(GENERAL_CHANNEL) # general channel ID
    await channel.send(f'Hi {member.name}, welcome to {member.guild.name}')

@bot.command(name='daily', help='Responds with the daily leetcode problem')
async def leetcode_daily(ctx): #ctx = context which holds channel/guild info
    await ctx.send(get_leetcode_daily())

bot.run(TOKEN)
