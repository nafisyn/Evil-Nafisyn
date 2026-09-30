import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="w")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
ALLOWED_USER_ID = 583206969544802315 # nafisyn

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user.name} is online")

@bot.command()
async def nafisay(
    ctx, *, message: str
     ):
    if ctx.author.id != ALLOWED_USER_ID:
        await ctx.message.delete()
        return

    await ctx.message.delete()
    await ctx.send(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)