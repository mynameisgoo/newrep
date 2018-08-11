import telebot
import requests
from config import token
import datetime
import time

from telebot import types

bot = telebot.TeleBot(token)

channel_name = "@cryptaisgood"
adw_post = "this is a test-message, who cares"
time = int(time.time())
post_time = datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')


def check():
    link = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (token, channel_name, adw_post)
    r = requests.get(link).json()
    # print(r)
    # print(r['ok'])
    if r['ok'] == True:
        return True
    else:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    if check() == True:
        bot.send_message(channel_name, adw_post)
        bot.send_message(message.chat.id, 'Постнул в канал %s рекламный пост "%s". Время размещения: %s, если по человечески: %s' % (channel_name, adw_post, time, post_time))
    else:
        bot.send_message(message.chat.id, 'Сорян, но бот не является админом группы')

bot.polling()




