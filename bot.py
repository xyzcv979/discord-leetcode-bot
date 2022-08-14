# bot.py
from email import message
import discord
from dotenv import load_dotenv
import os

# intents = discord.Intents.default()
# intents.message_content = True

load_dotenv('dev.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client() # connection to discord

@client.event # registers event
async def on_ready(): # once bot is online
    print(f'We have logged in as {client.user}')

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
    await message.channel.send(f'Hi {member.name}, welcome to {member.guild.name}')

client.run(TOKEN)
