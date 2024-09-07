from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.models import PdfContent, UrlContent
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



class QueryProcessor:


    
    def getAllContent(self,db:Session):
        try:
            pdf_records = db.query(PdfContent).all()
            url_records = db.query(UrlContent).all()

            print("PDF Records ",pdf_records)

            if not pdf_records:
                return []
            if not url_records:
                return []
            
            pdf_list = [pdf.pdf_content for pdf in pdf_records]
            url_list = [url.url_content for url in url_records]

            content_list = pdf_list + url_list
            return content_list

        except Exception as e:
            print(f"Error getting relevant Content: {e}")
            return None


    def getRelevantContent(self,query:str,db:Session):        

        content_list = self.getAllContent(db)
        if not content_list:
            return "No Content Available"
        vectorizer = TfidfVectorizer()

        pdf_tfidf = vectorizer.fit_transform(content_list)   
        query_tfidf = vectorizer.transform([query])        
        similarities = cosine_similarity(query_tfidf, pdf_tfidf)
        
        most_similar_index = np.argmax(similarities)
        
        return content_list[most_similar_index]

            
