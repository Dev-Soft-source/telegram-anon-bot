from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Text
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Telegram user_id
    username = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    banned = Column(Boolean, default=False)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False)  # Telegram user_id
    channel_message_id = Column(BigInteger, nullable=False)  # message ID in channel
    text = Column(Text, nullable=False)