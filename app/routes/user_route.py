from fastapi import APIRouter, Depends, status

from app.routes import get_db, Session
from app.schemas import BaseUser
from app.models import User

user_router = APIRouter()


# get user
@user_router.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=BaseUser)
def get_user(user: User, db:Session = Depends(get_db)):
    """gets a user"""
    found_user = db.query(user).filter(user.id == id).first()
    return found_user

# post user
@user_router.post("/users", status_code=status.HTTP_201_CREATED, response_model=BaseUser)
def create_user(new_user: BaseUser, db:Session = Depends(get_db)):
    """creates a user"""
    user = User(**new_user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# update user 
@user_router.put("/users/{id}", status_code=status.HTTP_200_OK, response_model=BaseUser)
def update_user(id:int, user: User, db:Session = Depends(get_db)):
    """updates a user"""
    found_user = db.query(user).filter(user.id == id).first()
    found_user = user
    db.commit()
    db.refresh(found_user)
    return found_user