from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Chat_Bot_3.keyboards.tours import make_row_keyboard
from Chat_Bot_3.keyboards.keyboards import kb1


router = Router()

available_tours = [
    "Водные туры",
    "Пешие туры",
    "Конные прогулки",
    "Горные походы"
]

available_kategory = ["Активный отдых", "Природа", "Культура и традиции"]

class ChoiceProfile(StatesGroup):
    tour = State()
    kategory = State()

@router.message(Command("tours"))
async def command_tours(message: types.Message, state: FSMContext):
    await message.answer(
        "Выбери тур",
        reply_markup=make_row_keyboard(available_tours))
    await state.set_state(ChoiceProfile.tour)


@router.message(ChoiceProfile.tour, F.text.in_(available_tours))
async def tour_chosen(message: types.Message, state: FSMContext):
    await state.update_data(my_tour=message.text)
    lst = await state.get_data()
    if "Водные туры" == lst['my_tour']:
        await message.answer('ОТЛИЧНО поплаваем :)\n\n'
                             '* Индивидуальный подход к каждому клиенту\n\n'
                             '* Опытные гиды со знанием местной природы и культуры\n\n'
                             '* Комфортное проживание в палатках или гостиницах\n\n'
                             '* Разнообразное питание и страховка участников')

    elif "Конные прогулки" == lst['my_tour']:
        await message.answer('Лошади уже ждут Вас!\n\n'
                             'Конные прогулки - это возможность уединиться с дикой природой и зарядиться энергией.')
    elif "Горные походы" == lst['my_tour']:
        await message.answer('Хороший выбор\n\n'
                             'Насладись красотой и величием пейзажей Алтая: гора Белуха, Телецкое озеро, Чуйская степь, Мультинские озера, районы: Горный Алтай, Майминский, Чемальский')
        await message.answer_dice(emoji="🎯")

    """async def button_handler(message: types.Message):
        if button_handler == 'Водные туры':
            await message.answer('ОТЛИЧНО поплаваем')
        elif message.text == 'Конные прогулки':
            await message.answer('Лошади уже ждут Вас')
        elif message.text == 'Горные походы':
            await message.answer('Хороший выбор')
            await message.answer_dice(emoji="🎯")
            # вызывает эмодзи по коду в строке ниже"""
        # text = "\U0001F601"
        # await message.answer(text)
        # вызывает random (игральный кубик)


    await message.answer(
        "Выбери категорию отдыха",
        reply_markup=make_row_keyboard(available_kategory))
    await state.set_state(ChoiceProfile.kategory)


@router.message(ChoiceProfile.tour)
async def tour_chosen_incorrect(message: types.Message):
    await message.answer(
        "Выбери тур",
        reply_markup=make_row_keyboard(available_tours))


@router.message(ChoiceProfile.kategory, F.text.in_(available_kategory))
async def kategory_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"Ваш тур: {user_data['my_tour']}\n"
                         f"Ваша категория: {message.text}\n\n"
                         f"Удачного отдыха!",
                         reply_markup=kb1)
    await state.clear()

@router.message(ChoiceProfile.kategory)
async def kategory_chosen_incorrect(message: types.Message):
    await message.answer(
        "Выбери категорию",
        reply_markup=make_row_keyboard(available_kategory))