from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from services.url_extractor import UrlContentExtractor

url_router = APIRouter()

@url_router.post("/")
def query_content(url: str, db:Session = Depends(get_db)):

    url_extractor_obj  = UrlContentExtractor()
    url_id,content = url_extractor_obj.getUrlContent(url,db)

    return {"chat_id": url_id,"message": content}
