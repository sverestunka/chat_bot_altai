import requests
from aiogram import types

async def get_random_image():
    # Замените на ваш API-ключ и URL-адрес API
    api_key = "7okDTNFNIXmIA5CKgNfbNQJ5sdoy2IbzWD42CFS0Snk"
    api_url = "https://api.unsplash.com/photos/random?query=altai-mountains"

    headers = {"Authorization": "Client-ID " + api_key}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        return json_response["urls"]["small"]
    else:
        return None

async def send_image(message: types.Message):
    image_url = await get_random_image()
    """if image_url is not None:
        await message.answer_photo(chat_id=message.chat.id, photo=image_url)
    else:
        await message.reply("Извините, не удалось получить изображение.")"""

def searchPhotos(message: types.Message):
    return send_image(message)


if __name__ == '__main__':
    searchPhotos()

 """  
    # Замените на ваш токен бота
    bot = Bot(token='YOUR_BOT_TOKEN')
    dp = Dispatcher(bot)

    dp.register_message_handler(start, commands=['start'])

    from aiogram import executor
    executor.start_polling(dp)

    dp.add_handler(CommandHandler('start', send_image))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
"""