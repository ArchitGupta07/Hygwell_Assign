from fastapi import APIRouter

url_router = APIRouter()

@url_router.post("/url")
def query_content(url: str):
    # Logic for querying the processed content using embeddings
    return {"message": f"Querying content for: {url}"}
