from typing import List
from fastapi import APIRouter, Depends, status
from app.schemas.post_schema import PostSchema
from ..models import PostModel
from app.utils.database import get_db
from sqlalchemy.orm import Session
post_router = APIRouter()

@post_router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostSchema)
def create_post(new_post: PostSchema, db: Session = Depends(get_db)):
    saved_post = PostModel(**new_post)
    db.add(saved_post)
    db.commit()
    db.refresh(saved_post)

@post_router.get("/posts", response_model=PostSchema)
def getpost(db: Session = Depends(get_db)) -> dict[str, List[PostModel]]:
    """fetches all posts"""
    posts = db.query(PostModel).all()
    return{"data": posts}
