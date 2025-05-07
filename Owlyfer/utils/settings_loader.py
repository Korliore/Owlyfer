from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Telegram(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    bot_token: str = Field(..., alias="TELEGRAM_BOT_TOKEN")
    channel_id: str = Field(..., alias="TELEGRAM_CHANNEL_ID")


class MongoDB(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    host: str = Field(..., alias="MONGO_INITDB_ROOT_HOST")
    port: int = Field(..., alias="MONGO_PORT")
    username: Optional[str] = Field(None, alias="MONGO_INITDB_ROOT_USERNAME")
    password: Optional[str] = Field(None, alias="MONGO_INITDB_ROOT_PASSWORD")
    db_name: str = Field(..., alias="MONGO_INITDB_DATABASE")


class AppSettings():
    log_path: str = "logs/"
    db_path: str = "database.db"


class Postgres(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    host: str = Field(..., alias="POSTGRES_HOST")
    port: int = Field(..., alias="POSTGRES_PORT")
    username: Optional[str] = Field(None, alias="POSTGRES_USER")
    password: Optional[str] = Field(None, alias="POSTGRES_PASSWORD")
    db_name: str = Field(..., alias="POSTGRES_DB")



try:
    telegram = Telegram()
    mongodb = MongoDB()
    app_settings = AppSettings()
except Exception as e:
    print(f"Ошибка загрузки параметров: {e}")
    print("Проверьте верность введенных данных")
    exit()
