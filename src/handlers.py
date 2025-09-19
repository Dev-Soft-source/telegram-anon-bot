from aiogram.types import Message
from aiogram import Router
from sqlalchemy.future import select
from src.database import SessionLocal
from src.models import User
from src import config

router = Router()

@router.message(commands=["start"])
async def cmd_start(message: Message):
    """Register or update user when they start the bot."""
    async with SessionLocal() as session:
        user = await session.get(User, message.from_user.id)

        if not user:
            user = User(
                id=message.from_user.id,
                username=message.from_user.username,
                is_admin=message.from_user.id in config.ADMIN_IDS
            )
            session.add(user)
        else:
            user.username = message.from_user.username  # update if changed

        await session.commit()

    role = "Admin ✅" if message.from_user.id in config.ADMIN_IDS else "User 👤"
    await message.answer(f"Welcome! You are registered.\nRole: {role}")
