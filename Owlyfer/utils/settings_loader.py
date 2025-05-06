import os
from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings
from typing import Optional


class Telegram(BaseSettings):
    bot_token: str = Field(..., env="TELEGRAM_BOT_TOKEN")
    channel_id: str = Field(..., env="TELEGRAM_CHANNEL_ID")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class MongoDB(BaseSettings):
    host: str = Field(..., env="mongo_host")
    port: int = Field(..., env="mongo_port")
    username: Optional[str] = Field(None, env="mongo_username")
    password: Optional[str] = Field(None, env="mongo_password")
    db_name: str = Field(..., env="mongo_db")

    class Config:
        env_file = ".env"


class AppSettings(BaseSettings):
    log_path: str = "logs/"
    db_path: str = "database.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


try:
    telegram = Telegram()
    mongodb = MongoDB()
    app_settings = AppSettings()
except Exception as e:
    print(f"Ошибка загрузки параметров: {e}")
    print("Проверьте верность введенных данных")
    exit()
