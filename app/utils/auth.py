from fastapi.security import oauth2
from passlib.context import CryptContext

oauth2_scheme = oauth2.OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain_password:str):
    """hash password"""
    return pwd_context.hash(plain_password)

def verify_password(plain_password:str, hashed_password:str):
    """verify password"""
    return pwd_context.verify(plain_password, hashed_password)
