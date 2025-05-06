from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.mongo import MongoStorage
from motor.motor_asyncio import AsyncIOMotorClient

from utils.log_worker import Logger
from utils.db_worker import DBWorker
from utils.settings_loader import telegram, mongodb, app_settings
from db import DBSessionMiddleware, async_session_factory


try:
    bot = Bot(token=telegram.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    client = AsyncIOMotorClient(
        host=mongodb.host,
        port=mongodb.port,
        username=mongodb.username,
        password=mongodb.password,
        connect=True,
    )
    dp = Dispatcher(storage=MongoStorage(client=client, db_name=mongodb.db_name))
    dp.message.middleware(DBSessionMiddleware(async_session_factory))
    db = DBWorker()
except Exception as ex:
    Logger.error(ex)
    exit()
