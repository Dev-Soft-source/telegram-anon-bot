import asyncio
import logging
from aiogram import Bot, Dispatcher
from src import config
from src.handlers import router
from src.database import engine, Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = config.bot
dp = Dispatcher()

# include routes
dp.include_router(router)

async def main():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        logger.info("Starting bot...")
        await dp.start_polling(bot)        
    finally:
        await bot.session.close()
    # Create tables
   
if __name__ == "__main__":
    asyncio.run(main())
