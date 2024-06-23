import asyncio
import logging

from aiogram import Bot, Dispatcher, types, fsm, handlers
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

import config
API_TOKEN = config.token
# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)
# Инициализация бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет, {name}", reply_markup=keyboard2)

@dp.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("Это справочная команда. Бот в разработке. Совсем скоро вы сможете воспользоваться новыми командами.")

@dp.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Я бот, могу повторять за тобой")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
