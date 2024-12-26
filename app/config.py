from dotenv import load_dotenv
import os
load_dotenv()
class settings:
    db_name = os.getenv('DB_NAME')
    db_host = os.getenv('DB_HOST')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')
    db_user = os.getenv('DB_USER')
    secret_key = os.getenv('SECRET_KEY')
    algorithm = os.getenv('ALGORITHM')
    access_token_expire_minutes = os.getenv('EXPIRE_MINUTES')