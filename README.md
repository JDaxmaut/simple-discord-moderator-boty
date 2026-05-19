![preview](https://raw.githubusercontent.com/JDaxmaut/simple-discord-moderator-boty/main/image.png)

# Discord Модератор Бот

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![discord.py](https://img.shields.io/badge/discord.py-2.0+-green.svg)

Бот для модерации Discord сервера. Автоматически удаляет сообщения с запрещёнными словами и выдаёт мут нарушителям.

---

## Команды

| Команда | Описание |
|---------|----------|
| `!ban @пользователь [причина]` | Бан пользователя на сервере |
| `!kick @пользователь [причина]` | Кик пользователя с сервера |

---

## Структура проекта

```
botmoderator/
├── main.py            # Запуск бота
├── config.py          # Настройки
├── requirements.txt   # Зависимости
└── cogs/
    ├── moderation.py  # Команды модерации (ban, kick)
    └── filters.py     # Фильтр мата и мут
```

---

## Установка

```bash
# Клонирование репозитория
git clone https://github.com/JDaxmaut/simple-discord-moderator-boty.git
cd simple-discord-moderator-boty

# Установка зависимостей
pip install -r requirements.txt

# Создание .env файла
echo DISCORD_TOKEN=твой_токен > .env
```

---

## Настройки

| Параметр | Описание | По умолчанию |
|----------|---------|--------------|
| `DISCORD_TOKEN` | Токен бота из Discord Developer Portal | — |
| `MUTE_TIME` | Время мута в минутах | 30 |
| `FORBIDDEN_WORDS` | Список запрещённых слов | см. config.py |

---

## Запуск

```bash
python main.py
```

---

## Технологии

- **discord.py** — библиотека для Discord API
- **Python 3.10+** — асинхронное программирование
- **Cogs** — модульная архитектура ботов

> Цель проекта: изучение асинхронного программирования и разработка Discord ботов.
