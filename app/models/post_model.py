from .base_model import Base
from sqlalchemy import Column
class UserModel(Base):
    __tablename__ = 'users'