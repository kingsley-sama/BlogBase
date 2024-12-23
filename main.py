#!/usr  /bin/env python3
"""this is the entry point of my fastapi app"""
from app.routes import post_router
from app.schemas.user_schema import BaseUser
from fastapi import FastAPI, status, APIRouter
from psycopg2.extras import RealDictCursor
import uvicorn

app = FastAPI()


app.include_router(post_router)


@app.get("/")
def root():
    """entry to the file"""
    user_id = 1
    log = {
        "message": "Welcome to BlogBase API",
        "description": """is a modern, lightweight, and powerful API for managing blog posts and users.""",
        "version": "1.0.0",
        "endpoints": {
            "/users": "Get a list of users.",
            f"/users/{user_id}": "Get details of a specific user.",
            "/docs": "API documentation (OpenAPI).",
            "/redoc": "Alternative API documentation."
        },
   "health_check": "API is running fine."
    }
    return log

"""auth route"""

"""users route"""


if __name__ == "__main__":
    uvicorn.run(app, host="5000", port=8000)

