from sqlalchemy.orm import Session

from ..models import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

def get_db():
    """function to get the database connection using sqlalchemy"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()