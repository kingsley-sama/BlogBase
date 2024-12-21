#!/usr/bin/env python3
"""this file defines my sequel base model"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')

SQLALCHEMY_URL = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'

engine = create_engine(SQLALCHEMY_URL)

Base = declarative_base()