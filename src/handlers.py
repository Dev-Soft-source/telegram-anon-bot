from aiogram.types import Message
from aiogram import Router
from sqlalchemy.future import select
from src.database import SessionLocal
from src.models import User, Comment
from aiogram.filters import Command
from src import config

router = Router()

# Existing start command
@router.message(Command("start"))
async def cmd_start(message: Message):
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
            user.username = message.from_user.username
        await session.commit()

    role = "Admin ✅" if message.from_user.id in config.ADMIN_IDS else "User 👤"
    await message.answer(f"Welcome! You are registered.\nRole: {role}")

# -----------------------------
# Anonymous posting
@router.message()  # catches any text message
async def anonymous_post(message: Message):
    """Relay user message to the channel anonymously."""
    if message.chat.type != "private":
        # Only allow private chat messages for anonymity
        return

    # Save comment in DB after posting
    async with SessionLocal() as session:
        # Post to the channel under bot identity
        print('ChannelID', config.CHANNEL_ID)
        sent_msg = await message.bot.send_message(
            chat_id=config.CHANNEL_ID,
            text=message.text
        )

        # Store mapping
        comment = Comment(
            user_id=message.from_user.id,
            channel_message_id=sent_msg.message_id,
            text=message.text
        )
        session.add(comment)
        await session.commit()

    await message.answer("✅ Your message was posted anonymously to the channel.")
