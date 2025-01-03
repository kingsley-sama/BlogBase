from pydantic import BaseModel, EmailStr
from typing import Optional

class BaseUser(BaseModel):
    """the base use detail, any other user related schemas will 
    inherit this schema 
    """
    name: str
    email:EmailStr
    user_name: str
    password: str
    user_type: str
    profile_img: Optional[str] = "/avatar.jpg"

class ReturnUser(BaseModel):
    """returns user detail"""
    name: str
    email:EmailStr
    user_name: str
    user_type: str
    profile_img: str



class Token(BaseModel):
    """token schema"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """token data schema"""
    email: Optional[str] = None
    user_type: Optional[str] = None

    