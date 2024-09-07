


def getAllContent(db:Session):
        
            pdf_records = db.query(PdfContent).all()
            url_records = db.query(UrlContent).all()