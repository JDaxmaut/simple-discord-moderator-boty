"""
Конфигурационный файл бота.
"""

import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MUTE_TIME = 30

FORBIDDEN_WORDS = [
    'badword', 'badwords', 'offensive', 'inappropriate',
    'example', 'placeholder', 'testword', 'sample',
]
