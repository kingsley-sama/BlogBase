#!/usr  /bin/env python3
"""this is the entry point of my fastapi app"""
from app.schmas.user_schema import BaseUser
from fastapi import FastAPI, status
from app.schmas.post_schema import PostSchema
import psycopg2
from psycopg2.extras import RealDictCursor
import uvicorn
from dotenv import load_dotenv
import os
import time
load_dotenv()
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
app = FastAPI()


try:
    conn = psycopg2.connect(host=db_host, database=db_name, 
                        user=db_user, password=db_password,
                         cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('db connected successfully')
except Exception as error:
    print("connecting to database failed")
    print(f"error: {error}")
    time.sleep(4)

def root():
    """entry to the file"""
    user_id = 1
    log = {
        "message": "Welcome to BlogBase API",
        "description": """is a modern, lightweight, and powerful API for managing blog posts and users.""",
        "version": "1.0.0",
        "endpoints": {
            "/users": "Get a list of users.",
            "/users/{user_id}": "Get details of a specific user.",
            "/docs": "API documentation (OpenAPI).",
            "/redoc": "Alternative API documentation."
        },
   "health_check": "API is running fine."
    }
    return log

"""auth route"""

"""users route"""
@app.post("/users")
def create_user(user:BaseUser):
    print(user.dict())
    return{"this is the user gotten": user}

"""posts routes"""

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: PostSchema):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING *""", (new_post.title, new_post.content, new_post.published))
    my_post = cursor.fetchone()
    conn.commit()
    return{"this are the current posts": my_post}

@app.get("/posts")
def getpost():
    """fetches all posts"""
    cursor.execute("""SELECT * FROM posts""")
    my_post = cursor.fetchall()
    return{'data': my_post}

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    """gets a post by id"""
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    my_post = cursor.fetchone()
    return{'dat': my_post}

@app.put("/posts/{id}")
def update_post(id: int, post: PostSchema):
    """gets a post by id"""
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id=%s RETURNING *""",(post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    return{f"updated post whith id {id}": updated_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    """deletes a post"""
    cursor.execute("""DELETE * FROM posts WHERE id=%s RETURNING *""", (str(id),))

    return f"post with id {id} deleted successfully"


if __name__ == "__main__":
    uvicorn.run(app, host="5000", port=8000)

