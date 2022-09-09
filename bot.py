# bot.py
from enum import IntEnum
import discord
from dotenv import load_dotenv
import os
from leetcode_requests import *
import datetime

from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
# intents = discord.Intents.default()
# intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

GENERAL_CHANNEL = 1007826049347891201
LEETCODE_CHANNEL = 1008072276396216342

@bot.event # registers event
async def on_ready(): # once bot is online
    print(f'{bot.user} connected to Discord!')
    if not run_job.is_running():
        run_job.start()

# @bot.event
# async def on_message(message): # on receiving a message
#     if message.author == bot.user: # doesn't do anything is message is from bot
#         return

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(GENERAL_CHANNEL) # general channel ID
    await channel.send(f'Hi {member.name}, welcome to {member.guild.name}')

daily_time = datetime.time(hour=10, minute=0, second=0)
@tasks.loop(time=daily_time)
async def run_job():
    await bot.wait_until_ready()
    daily_url = get_leetcode_daily()
    channel = bot.get_channel(LEETCODE_CHANNEL)
    await channel.send(f'Daily problem: {daily_url}')


@bot.command(name='daily', help='Responds with the daily leetcode problem')
async def leetcode_daily(ctx): #ctx = context which holds channel/guild info
    await ctx.send(get_leetcode_daily())

@bot.command(name='random', help='random leetcode problem')
async def leetcode_random(ctx):
    await ctx.send(get_random_question())

@bot.command(name='random easy', help='random easy leetcode problem')
async def leetcode_random_easy(ctx):
    await ctx.send(get_random_difficulty("EASY"))

@bot.command(name='random medium', help='random medium leetcode problem')
async def leetcode_random_medium(ctx):
    await ctx.send(get_random_difficulty("MEDIUM"))
    
@bot.command(name='random hard', help='random hard leetcode problem')
async def leetcode_random_hard(ctx):
    await ctx.send(get_random_difficulty("HARD"))


@bot.command(name='random array', help='random array leetcode problem')
async def leetcode_random_array(ctx):
    await ctx.send(get_random_tag("array"))

@bot.command(name='random string', help='random string leetcode problem')
async def leetcode_random_string(ctx):
    await ctx.send(get_random_tag("string"))

@bot.command(name='random dp', help='random dynamic-programming leetcode problem')
async def leetcode_random_dp(ctx):
    await ctx.send(get_random_tag("dynamic-programming"))

@bot.command(name='random dfs', help='random depth-first-search leetcode problem')
async def leetcode_random_dfs(ctx):
    await ctx.send(get_random_tag("depth-first-search"))

@bot.command(name='random bfs', help='random breadth-first-search leetcode problem')
async def leetcode_random_bfs(ctx):
    await ctx.send(get_random_tag("breadth-first-search"))

@bot.command(name='random tree', help='random tree leetcode problem')
async def leetcode_random_tree(ctx):
    await ctx.send(get_random_tag("tree"))

@bot.command(name='random graph', help='random graph leetcode problem')
async def leetcode_random_graph(ctx):
    await ctx.send(get_random_tag("graph"))

@bot.command(name='random backtracking', help='random backtracking leetcode problem')
async def leetcode_random_backtracking(ctx):
    await ctx.send(get_random_tag("backtracking"))

@bot.command(name='random linkedlist', help='random linked-list leetcode problem')
async def leetcode_random_linkedlist(ctx):
    await ctx.send(get_random_tag("linked-list"))


bot.run(TOKEN)
