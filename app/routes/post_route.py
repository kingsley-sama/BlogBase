from fastapi import APIRouter, Depends, status
from app.schmas.post_schema import PostSchema
from app.utils.database import get_db
post_router = APIRouter()
from sqlalchemy.orm import Session
@post_router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: PostSchema, db: Session = Depends(get_db)):

    return{"this are the current posts"}

@post_router.get("/posts")
def getpost(db: Session = Depends(get_db)):
    """fetches all posts"""
    pass

@post_router.get("/posts/{id}")
def get_post_by_id(id: int):
    """gets a post by id"""
    pass

@post_router.put("/posts/{id}")
def update_post(id: int, post: PostSchema):
    """gets a post by id"""
    pass

@post_router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    """deletes a post"""
    pass

