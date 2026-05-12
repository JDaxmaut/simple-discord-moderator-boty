"""
Главный файл бота. Запуск и загрузка расширений.
"""

import discord
from discord.ext import commands
from config import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    """При запуске загружаем Cogs."""
    print(f"{bot.user.name} запущен")
    
    try:
        await bot.load_extension("cogs.moderation")
        await bot.load_extension("cogs.filters")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")


bot.run(DISCORD_TOKEN)
