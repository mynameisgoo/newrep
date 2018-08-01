import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.token)

def keyboard1():
    """
    клавиатура со старта
    :return: кнопки "Просмотреть заявки", "Создать заявку"
    """
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Просмотреть заявки', 'Создать заявку')
    global key1
    key1 = keyboard

def keyboard2():
    """
    :return: Вернуться, Следующая страница
    """
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Вернуться', callback_data='quit')
    btn2 = types.InlineKeyboardButton('Cледующая страница', callback_data='next')
    keyboard.add(btn1, btn2)
    global key2
    key2 = keyboard

def keyboard3():
    """
    :return: Вернуться, Предыдущая страница, Следующая страница
    """
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Вернуться', callback_data='quit')
    btn2 = types.InlineKeyboardButton('Предыдущая страница', callback_data='back')
    btn3 = types.InlineKeyboardButton('Cледующая страница', callback_data='next')
    keyboard.add(btn1, btn2, btn3)
    global key3
    key3 = keyboard

@bot.message_handler(commands=['start'])
def start(message):
    keyboard1()
    bot.send_message(message.chat.id, 'Привет, я бот, можешь смотреть или создать заявку', reply_markup=key1)

@bot.message_handler(func=lambda message: message.text == 'Просмотреть заявки', content_types=['text'])
def orders(message):
    keyboard2()
    bot.send_message(message.chat.id, 'Заявки:', reply_markup=key2)

@bot.callback_query_handler(func=lambda call: call.data == 'quit')
def start(call):
    keyboard1()
    bot.send_message(chat_id=call.message.chat.id, text='Привет, я бот, можешь смотреть или создать заявку', reply_markup=key1)

@bot.callback_query_handler(func=lambda call: call.data == 'next')
def callback_next(call):
    keyboard3()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Заявки, страница ', reply_markup=key3)

@bot.callback_query_handler(func=lambda call: call.data == 'back')
def callback_next(call):
    # num = num - 1
    keyboard3()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Заявки, страница ', reply_markup=key3)




@bot.message_handler(func=lambda message: message.text == 'Создать заявку', content_types=['text'])
def name(message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('как админ', 'как рекламодатель')
    bot.send_message(message.chat.id, 'Как админ или как рекламодатель?', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'как админ', content_types=['text'])
def name(message):
    bot.send_message(message.chat.id, 'Введи название группы')

@bot.message_handler(func=lambda message: message.text == 'как рекламодатель', content_types=['text'])
def name(message):
    bot.send_message(message.chat.id, 'Введи название группы')

@bot.message_handler(func=lambda message: message.text == 'example', content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Введи свой никнейм через собаку')

@bot.message_handler(func=lambda message: message.text == '@example', content_types=['text'])
def username(message):
        bot.send_message(message.chat.id, 'Введи сумму в рублях в цифрах')

@bot.message_handler(func=lambda message: message.text == '1000', content_types=['text'])
def money(message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Вернуться назад')
    bot.send_message(message.chat.id, 'Отлично, заявка создана', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Вернуться назад', content_types=['text'])
def start(message):
    keyboard1()
    bot.send_message(message.chat.id, 'Привет, я бот, можешь смотреть или создать заявку', reply_markup=key1)

# bot.send_message()


bot.polling(none_stop=True, interval=0)