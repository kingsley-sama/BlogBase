#!/usr/bin/env python3
"""defines the user model"""
from sqlalchemy import Column, Integer, String
from .base_model import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    user_type = Column(String, default=True)
