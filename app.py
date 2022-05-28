from aiogram.utils import executor
from config import ADMIN_ID
from loader import bot


async def on_shutdown(dp):
    bot.close()

async def on_start(dp):
    await bot.send_message(ADMIN_ID, "Bot started")

if __name__ == '__main__':
    from main import dp
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_start)