import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')

list_button_text = ['2023', '2022', '2021', '2020','2019', '2018', '2017', '2016']
mem_list_bot = {
    '2023' : 'https://www.myinstants.com/media/sounds/ronaldo-siuuuu.mp3',
    '2022' : 'https://zvukogram.com/mp3/cats/1200/sanechka-snimaesh.mp3',
    '2021' : 'https://zvukogram.com/mp3/cats/1200/ahaha-razryivnaya.mp3',
    '2020' : 'https://zvukogram.com/mp3/cats/1200/o-povezlo-povezlo.mp3',
    '2019' : 'https://zvukogram.com/mp3/cats/1200/es-minus-ehuuu.mp3',
    '2018' : 'https://zvukogram.com/mp3/cats/1200/ya-musulman.mp3',
    '2017' : 'https://www.myinstants.com/media/sounds/yt1s_NSjFWNC.mp3',
    '2016' : 'https://zvukogram.com/mp3/cats/1200/otdai-salo.mp3'

}

#создание меню кнопок
@bot.message_handler(commands=['help',  'start'])
async def send_hello(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Вы найдете здесь все популярные мемы!', disable_notification=True, protect_content=True)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    one_b = '2021⚡'
    two_b = '2020🔥'
    three_b = '2019💧'
    four_b = '2018⚡'
    five_b = '2017✨'
    six_b = '2016⚡'
    seven_b = '2022✨'
    eight_b = '2023⚡'
    markup.add(eight_b, seven_b, one_b, row_width=3)
    markup.add(two_b, three_b, row_width=2)
    markup.add(four_b, five_b, six_b, row_width=3)
    await bot.send_message(chat_id, '✨Menu✨', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
async def handle_message(message):
    print(message.text)
    chat_id = message.chat.id
    text = message.text
    for i in range(len(list_button_text)):
        if list_button_text[i] in text:
            await bot.send_audio(chat_id, mem_list_bot[list_button_text[i]])
            break
    else:
        await bot.send_message(chat_id, 'Это появится позже!')

import asyncio
asyncio.run(bot.polling())