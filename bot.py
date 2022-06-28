import requests
import random
import telebot
from bs4 import BeautifulSoup as BS

URL = 'https://kaschenko.pythonanywhere.com/'
API_KEY = 'TOKEN'


def parser(url):
    r = requests.get(url)
    soup = BS(r.text, 'html.parser')
    post = soup.find_all('p', class_='justify')
    pure_post = [i.text for i in post]
    return pure_post


list_of_post = parser(URL)
bot = telebot.TeleBot(API_KEY, threaded=False)


@bot.message_handler(commands=['начать'])
def hello(message):
    bot.send_message(
        message.chat.id,
        'Привет! Что-бы получить рандомный пост с сайта'
        ' https://kaschenko.pythonanywhere.com/ напишите "пост"'
    )


@bot.message_handler(content_types=['text'])
def posts(message):
    if message.text.lower() in 'пост':
        bot.send_message(message.chat.id, list_of_post)
        random.shuffle(list_of_post)
    else:
        bot.send_message(
            message.chat.id,
            'Напишите слово "пост",что-бы получить рандомный'
            ' пост с сайта https://kaschenko.pythonanywhere.com/'
        )


bot.polling(none_stop=True, interval=0)
