from .base_model import Base
from sqlalchemy import Column, Integer, String, Boolean

class PostModel(Base):
    __tablename__ = 'posts'
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=True)