from sqlalchemy import Column, Integer, String, Text
from database import Base

class ChatContent(Base):
    __tablename__ = "chat_contents"

    chat_id = Column(Integer, primary_key=True, index=True)
    url_content = Column(Text, nullable=False)
