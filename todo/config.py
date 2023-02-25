import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Класс для подгрузки переменных окружения"""
    app_name = os.getenv("NAME_APP")
    db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

    """Класс для построения пути до файла .env"""
    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
