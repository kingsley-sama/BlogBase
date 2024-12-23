from sqlalchemy.orm import Session
import models

from models import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():
    """function to get the database connection using sqlalchemy"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()