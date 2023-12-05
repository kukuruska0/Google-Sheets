from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

import handlers

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

dp.register_message_handler(handlers.start_cmd, commands=['start'])
dp.register_message_handler(handlers.save_data,(lambda message: types.Message))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
