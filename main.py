import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from cogwatch import Watcher


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')  

    watcher = Watcher(bot, path="commands", debug=False, preload=True)
    await watcher.start()

async def on_reload(cog):
    print(f'Reloaded {cog}')

async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

bot.run(TOKEN)