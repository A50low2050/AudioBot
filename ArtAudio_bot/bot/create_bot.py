from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Dbase import create_db

API_TOKEN = TOKEN

# Create Database
create_db()


def launch_bot():
    print('Бот успешно запущен')


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

