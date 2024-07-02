import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram.types.dice import DiceEmoji


from keyboards import kb1
from randomfox import fox

import config
API_TOKEN = config.token
# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)
# Инициализация бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp = Dispatcher()


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

@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.reply(f"Держи лису, {name}")
    # await message.answer_photo(photo=img_fox)
    await bot.send_photo(message.from_user.id, photo=img_fox)


@dp.message(F.text)
async def msg_echo(message: types.Message):
    print(message.text)
    name = message.chat.first_name
    if 'hello' in message.text.lower() or 'привет' in message.text.lower() or 'hi' in message.text.lower() or 'здравствуйте' in message.text.lower() or 'добрый вечер' in message.text.lower() or 'добрый день' in message.text.lower() or 'доброе утро' in message.text.lower() or 'доброй ночи' in message.text.lower():
        await message.reply(f"Приветствую, {name}")
    elif 'by' in message.text.lower() or 'пока' in message.text.lower():
        await message.reply(f"До свидания, {name}")
    elif 'как дела' in message.text.lower():
        # вызывает эмодзи по коду в строке ниже
        """text = "\U0001F601"
        await message.answer(text)"""
        # вызывает random (игральный кубик)
        await message.answer_dice(emoji="🎯")
    else:
        await message.answer(f'Ты написал - {message.text}', reply_markup=kb1)
"""@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)"""

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
