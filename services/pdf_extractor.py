from pdfminer.high_level import extract_text
from io import BytesIO
from sqlalchemy.exc import SQLAlchemyError
from utils.helper import clean_content
from sqlalchemy.orm import Session
from models.models import PdfContent


class PdfContentExtractor:

    def getPdfContent(self, file_name, file, db:Session):
        try:
            pdf_content = BytesIO(file)
            text = extract_text(pdf_content)
            content = clean_content(text)

            pdf_id = self.uploadPdfContent(file_name,content, db)
            return pdf_id, content
        
        except Exception as e:
            print(f"Error extracting PDF content: {e}")
            return None
        
    def uploadPdfContent(self,file_name, file_content, db:Session):
        try:
            db_content = PdfContent(file_name=file_name, pdf_content=file_content)
            
            db.add(db_content)
            db.commit()
            
            db.refresh(db_content)
            
            print(f"Inserted content for pdf: {file_name} with ID: {db_content.pdf_id}")
            return db_content.pdf_id
        
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error inserting content: {e}")
            return None
        
        

    