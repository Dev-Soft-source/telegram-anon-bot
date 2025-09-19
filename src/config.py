import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file into os.environ


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./anonbot.db")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing from .env file")
