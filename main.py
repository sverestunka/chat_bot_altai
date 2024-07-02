import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.filters import CommandObject

import config
API_TOKEN = config.token
# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)
# Инициализация бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp = Dispatcher()

"""button1 = types.KeyboardButton(text='info')
button2 = types.KeyboardButton(text='help')
kb = [
    [button1, button2]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)"""

@dp.message(F.text.lower() == "stop!")
async def with_puree(message: types.Message):
    await message.reply("Стоп машина!!")
@dp.message(F.text.lower() == "start!")
async def without_puree(message: types.Message):
    await message.reply("Поехали!")
@dp.message(F.animation)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Это справочная команда. Бот в разработке. Совсем скоро вы сможете воспользоваться новыми командами.")

@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer("Я бот, могу повторять за тобой")


@dp.message(F.text)
async def msg_echo(message: types.Message):
    print(message.text)
    name = message.chat.first_name
    if 'hello' in message.text.lower():
        await message.reply(f"И тебе привет, {name}")
    if 'by' in message.text.lower():
        await message.reply(f"Пока, {name}")
    await message.answer(message.text)
"""@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)"""

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
