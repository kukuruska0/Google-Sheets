import os

from aiogram import types

from classes import SaveUserData


async def start_cmd(message: types.Message):
    await message.answer('Welcome!')


async def save_data(message: types.Message):
    data = SaveUserData(message.from_user.first_name, message.from_user.username, message.chat.id, message.text)
    data.insert(client='ServiceData.json', url=os.getenv('SPREADSHEET_URL'))
    