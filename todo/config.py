import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

# Класс для подгрузки переменных окружения
class Settings(BaseSettings):
    app_name: str = os.getenv("NAME_APP")
    db_url: str = os.getenv("SQLALCHEMY_DATABASE_URL")

# Класс для построения пути до файла .env
    class Config:
        env_file: str = "../.env"
        env_file_encoding: str = "utf-8"


settings = Settings()
