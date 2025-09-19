from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Telegram user_id
    username = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    banned = Column(Boolean, default=False)
