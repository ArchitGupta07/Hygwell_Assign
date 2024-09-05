from fastapi import APIRouter, File, UploadFile

pdf_router = APIRouter()

@pdf_router.post("/pdf")
def process_pdf(file: UploadFile = File(...)):
    # Logic for processing the PDF
    return {"message": "PDF processed successfully"}
