from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from services.chatBot import QueryProcessor

chat_router = APIRouter()

@chat_router.post("/")
def process_query(query: str, db:Session = Depends(get_db)):

    query_processor_obj = QueryProcessor()
    relevant_content = query_processor_obj.getRelevantContent(query, db)
    
    return {"message": relevant_content}
