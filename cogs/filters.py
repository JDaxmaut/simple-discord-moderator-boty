"""
Фильтр мата: автоматическая проверка сообщений и мут.
"""

import discord
from discord.ext import commands
import re
from datetime import timedelta
from config import FORBIDDEN_WORDS, MUTE_TIME


class Filters(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Не получает self, можно вызывать без создания объекта
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Нормализует текст для проверки:
        - нижний регистр
        - удаление разделителей (пробелы, точки, тире)
        - замена цифр на буквы (leet speak)
        """
        text = text.lower()
        text = re.sub(r'[.\s_\-]', '', text)
        text = re.sub(r'[0134578]', lambda m: {'0':'o','1':'i','3':'e','4':'a','5':'s','7':'t','8':'b'}[m.group()], text)
        
        return text

    # Не получает self, можно вызывать без создания объекта
    @staticmethod
    def is_bad_message(text: str) -> bool:
        """Проверяет сообщение на содержание запрещенных слов."""
        cleaned = Filters.clean_text(text)
        return any(word in cleaned for word in FORBIDDEN_WORDS)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        # Пропускаем админов
        if message.author.guild_permissions.administrator:
            return
        
        if Filters.is_bad_message(message.content):
            await message.delete()
            
            try:
                await message.author.timeout(
                    timedelta(minutes=MUTE_TIME),
                    reason="Использование запрещенных слов"
                )
            except discord.Forbidden: 
		# Если у бота не хватило прав (например, нарушитель — админ или овнер)
                pass
            
            embed = discord.Embed(
                title="Сообщение удалено",
                description=f"{message.author.mention}, мут на {MUTE_TIME} мин.",
                color=discord.Color.dark_red()
            )
            await message.channel.send(embed=embed)
        
        await self.bot.process_commands(message)
	# Без этой строки бот застрянет на проверке мата и перестанет реагировать на команды


async def setup(bot: commands.Bot):
    await bot.add_cog(Filters(bot))
