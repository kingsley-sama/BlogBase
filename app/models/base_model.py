#!/usr/bin/env python3
"""this file defines my sequel base model"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models import settings

SQLALCHEMY_URL = f'postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}'

engine = create_engine(SQLALCHEMY_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()