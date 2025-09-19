import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

# get bot_token
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./bot.db")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing from .env file")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

# get channel_id
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
if not CHANNEL_ID:
    raise ValueError("CHANNEL_ID is missing from .env")