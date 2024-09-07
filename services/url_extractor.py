import requests
from bs4 import BeautifulSoup
from utils.helper import clean_content
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.models import UrlContent 

class UrlContentExtractor:   


    def UploadUrlContent(self,url:str, content:str, db:Session):
        try:
            db_content = UrlContent(url=url, url_content=content)
            
            db.add(db_content)
            db.commit()
            
            db.refresh(db_content)
            
            print(f"Inserted content for URL: {url} with ID: {db_content.url_id}")
            return db_content.url_id
        
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error inserting content: {e}")
            return None

    def getUrlContent(self, url:str, db:Session):
        try:
            response = requests.get(url)
            response.raise_for_status() 
            soup = BeautifulSoup(response.content, "html.parser")
            content = soup.get_text(separator=" ") 
            content = clean_content(content)

            url_id = self.UploadUrlContent(url, content, db)

            return url_id, content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from {url}: {e}")
            return None
        



