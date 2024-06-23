import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import config
API_TOKEN = config.token
# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)
# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")

@dp.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("Это справочная команда. Бот в разработке. Совсем скоро вы сможете воспользоваться новыми командами.")

@dp.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Я бот, созданный для помощи вам. Я могу отвечать на ваши вопросы, помогать вам узнавать новую информацию и многое другое. Просто напишите мне!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
