
from db.db import engine, Base
from models import models


def init_db():
    Base.metadata.create_all(bind=engine)