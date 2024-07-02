from aiogram import types

button1 = types.KeyboardButton(text='/info')
button2 = types.KeyboardButton(text='/help')
button3 = types.KeyboardButton(text='start!')
button4 = types.KeyboardButton(text='stop!')
button5 = types.KeyboardButton(text='Покажи лису')
button6 = types.KeyboardButton(text='Закрыть')
keyword1 = [
    [button1, button2],
    [button3, button4],
    [button5, button6]
]
kb1 = types.ReplyKeyboardMarkup(keyboard=keyword1, resize_keyboard=True)
