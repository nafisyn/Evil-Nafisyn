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

bot = commands.Bot(command_prefix="/", intents=intents)
ALLOWED_USER_ID = 583206969544802315 # nafisyn

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user.name} is online")

@bot.tree.command(
        name="say",
         description=f"Make the bot say something"
         )
async def say(
    interaction: discord.Interaction,
     message: str
     ):
    if interaction.user.id != ALLOWED_USER_ID:
        await interaction.response.send_message(
            "Only nafisyn can use this command idiot",
            ephemeral=True
        )
        return
    
    await interaction.response.send_message(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)