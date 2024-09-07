from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from db.db import Base
import uuid

class UrlContent(Base):
    __tablename__ = "UrlContent"

    url_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4, index=True)
    url = Column(String(255), nullable=False)
    url_content = Column(Text, nullable=False, default="No Data")

class PdfContent(Base):
    __tablename__ = "PdfContent"

    pdf_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4, index=True)
    file_name = Column(String(255), nullable=False)
    pdf_content = Column(Text, nullable=False)

class ChatContent(Base):
    __tablename__ = "ChatQueries"

    chat_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4, index=True)
    query = Column(Text, nullable=False)
