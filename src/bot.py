import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./anonbot.db")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing from .env file")

# Initialize bot and dispatcher
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)
dp = Dispatcher()

# /start command (everyone)
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("👋 Hello! Bot is running.")

# /admin command (admins only)
@dp.message(Command("admin"))
async def admin_handler(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.reply("❌ You are not authorized to use this command.")
        return

    await message.reply("✅ Welcome, admin!")

# Main function to run the bot
async def main():
    print("INFO: Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
