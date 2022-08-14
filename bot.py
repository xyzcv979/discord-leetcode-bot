# bot.py
import discord
from dotenv import load_dotenv
import os

# intents = discord.Intents.default()
# intents.message_content = True

load_dotenv('dev.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if 'short' in message.content:
        await message.channel.send("Emily is short!")

client.run(TOKEN)
