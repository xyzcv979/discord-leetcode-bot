# bot.py
import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client() # connection to discord

GENERAL_CHANNEL = 1007826049347891201
LEETCODE_CHANNEL = 1008072276396216342

@client.event # registers event
async def on_ready(): # once bot is online
    print(f'{client.user} connected to Discord!')

@client.event
async def on_message(message): # on receiving a message
    if message.author == client.user: # doesn't do anything is message is from bot
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if 'emily' in message.content or 'Emily' in message.content:
        await message.channel.send("Emily is short!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(GENERAL_CHANNEL) # general channel ID
    await channel.send(f'Hi {member.name}, welcome to {member.guild.name}')

client.run(TOKEN)
