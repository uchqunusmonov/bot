from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

