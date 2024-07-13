from aiogram import Router, types, F
from aiogram.filters.command import Command
from random import randint

from Chat_Bot_3.keyboards.keyboards import kb1, kb2
from Chat_Bot_3.utilits.randomfox import fox
from Chat_Bot_3.utilits.foto_altai import altai_foto

router = Router()


@router.message(F.text.lower() == "stop!")
async def with_puree(message: types.Message):
    await message.reply("Стоп машина!!")
@router.message(F.text.lower() == "start!")
async def without_puree(message: types.Message):
    await message.answer(f'Выбери меню', reply_markup=kb1)
@router.message(F.animation)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("С помощью кнопок меню можно узнать:\n"
                         "/info - ссылка на сайт\n"
                         "/tour - выбрать интересующий тур и прочитать о нем\n"
                         "/foto - увидеть фотографии с Алтая\n"
                         "/еще - перейти в след.меню\n")
    await message.answer(f'Выбери меню', reply_markup=kb1)
@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer("https://vsasite.tilda.ws/")
    await message.answer(f'Выбери меню', reply_markup=kb1)
@router.message(Command("start"))
async def cmd_start(message: types.Message):
     await message.answer(f'Выбери меню', reply_markup=kb1)
@router.message(Command("еще"))
async def cmd_info(message: types.Message):
    await message.answer(f'Выбери меню', reply_markup=kb2)

@router.message(F.text.lower() == "num")
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}", reply_markup=kb2)

@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.reply(f"Держи лису, {name}")
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)

@router.message(Command("foto"))
@router.message(F.text.lower() == "фото")
@router.message(F.text.lower() == "алтай")
async def cmd_altai(message: types.Message):
    name = message.chat.first_name
    img_altai = altai_foto()
    await message.reply(f"Вот фото Алтая, {name}")
    await message.answer_photo(photo=img_altai)
    await message.answer(reply_markup=kb1)
    # await bot.send_photo(message.from_user.id, photo=img_altai)


@router.message(F.text)
async def msg_echo(message: types.Message):
    print(message.text)
    name = message.chat.first_name
    if 'hello' in message.text.lower() or 'привет' in message.text.lower() or 'hi' in message.text.lower() or 'здравствуйте' in message.text.lower() or 'добрый вечер' in message.text.lower() or 'добрый день' in message.text.lower() or 'доброе утро' in message.text.lower() or 'доброй ночи' in message.text.lower():
        await message.reply(f"Приветствую, {name}")
    elif 'by' in message.text.lower():
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


