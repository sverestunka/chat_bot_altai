from aiogram import types

button1 = types.KeyboardButton(text='/info')
button2 = types.KeyboardButton(text='/help')
button3 = types.KeyboardButton(text='/start')
button4 = types.KeyboardButton(text='stop!')
button5 = types.KeyboardButton(text='Покажи лису')
button6 = types.KeyboardButton(text='/tours')
button7 = types.KeyboardButton(text='num')
button8 = types.KeyboardButton(text='/foto')
button9 = types.KeyboardButton(text='/еще')

keybord1 = [
    [button1, button6, button9],
    [button2, button8]
]

keybord2 = [
    [button5, button3, button7]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keybord1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keybord2, resize_keyboard=True)