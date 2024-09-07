
from fastapi import FastAPI
from routes import chat, pdf_processing, url_processing
from fastapi.middleware.cors import CORSMiddleware 
from contextlib import asynccontextmanager
from db.init_db import init_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("hello")
    init_db()
    yield
   

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(url_processing.url_router, prefix="/url")
app.include_router(pdf_processing.pdf_router, prefix="/pdf")
app.include_router(chat.chat_router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "Backend service is up and running"}