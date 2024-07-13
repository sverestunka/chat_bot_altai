from aiogram import types

button1 = types.KeyboardButton(text='/info')
button2 = types.KeyboardButton(text='/help')
button3 = types.KeyboardButton(text='start!')
button4 = types.KeyboardButton(text='stop!')
button5 = types.KeyboardButton(text='Покажи лису')
button6 = types.KeyboardButton(text='Закрыть')
button7 = types.KeyboardButton(text='num')
keybord1 = [
    [button1, button2],
    [button3, button4],
]

keybord2 = [
    [button5, button6, button7]
]
kb1 = types.ReplyKeyboardMarkup(keyboard=keybord1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keybord2, resize_keyboard=True)