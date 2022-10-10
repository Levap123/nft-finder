import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    dbname = os.getenv("DB_NAME")
    user_db = os.getenv("USER_NAME_DB")
    password_db = os.getenv("PASSWORD_DB")
    api_key = os.getenv("API_SECRET_KEY")
    api_id = os.getenv("API_KEY_ID")
    port = "8080"
