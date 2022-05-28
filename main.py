from aiogram import Bot, Dispatcher, types
from loader import dp

@dp.message_handler(commands=['start'])
async def initial_message(message:types.Message):
    first_name = message.from_user.first_name
    text = f'Assalomu Alaykum, {first_name}!'
    await message.answer(text)

@dp.message_handler()
async def second_message(message:types.Message):
    message1 = message.text
    text = f"Siz yuborgan xabar: <b>{message1}</b>"
    await message.answer(text)

