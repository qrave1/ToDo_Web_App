import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


# Класс для подгрузки переменных окружения
class Settings(BaseSettings):
    app_name = os.getenv("NAME_APP")
    db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

    # Класс для построения пути до файла .env
    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
