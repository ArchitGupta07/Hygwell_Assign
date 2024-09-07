from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db import get_db
from services.pdf_extractor import PdfContentExtractor

pdf_router = APIRouter()

@pdf_router.post("/")
async def process_pdf(file: UploadFile = File(...), db:Session = Depends(get_db)):

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")    
    
    file_data = await file.read()
    pdf_extractor_obj = PdfContentExtractor()
    pdf_id, content = pdf_extractor_obj.getPdfContent(file.filename,file_data,db)


    return {"chat_id":pdf_id, "message": content}
