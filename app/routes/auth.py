from curses.ascii import HT
from fastapi import APIRouter, Depends, HTTPException, status



auth_route = APIRouter(tags="Auth")


@auth_route.get("/login")
def login_user(user:User):
    # fetch user
    user = "user"
    if not user:
        raise HTTPException
    # validate user

    return "user logged in"
