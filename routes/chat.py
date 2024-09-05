from fastapi import APIRouter

chat_router = APIRouter()

@chat_router.post("/chat")
def process_url(query: str):
    # Logic for processing the URL
    return {"message": f"Processed URL: {query}"}
