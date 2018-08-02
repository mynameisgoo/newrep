from config import token
import telebot
from telebot import types


bot = telebot.TeleBot(token)

def keyboard_start():
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Рекламодатель', 'Админ')
    return keyboard

def keyboard_main():
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Создать заявку', 'Смотреть заявки')
    return keyboard

def keyboard_back_to_start():
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Назад')
    return keyboard




@bot.message_handler(commands=['start'])
def handle(message):
    bot.send_message(message.chat.id, 'Кем будешь?', reply_markup=keyboard_start())


@bot.message_handler(func= lambda message: message.text == 'Рекламодатель', content_types=['text'])
def ad_order(message):
    bot.send_message(message.chat.id, 'Выбирай, что хочешь', reply_markup=keyboard_main())

@bot.message_handler(func= lambda message: message.text == 'Админ', content_types=['text'])
def admin_order(message):
    bot.send_message(message.chat.id, 'Выбирай, что хочешь', reply_markup=keyboard_main())

@bot.message_handler(func= lambda message: message.text == 'Создать заявку', content_types=['text'])
def create_order(message):
    keyboard = types.ReplyKeyboardMarkup(True, )
    keyboard.row('Юзернейм')
    bot.send_message(message.chat.id, 'Введи свой рекламный текст, как отправишь - жми кнопку Юзернейм', reply_markup=keyboard)
    # здесь вносится рекламный текст в БД

@bot.message_handler(func= lambda message: message.text == 'Юзернейм', content_types=['text'])
def username(message):
    keyboard = types.ReplyKeyboardMarkup(True, )
    keyboard.row('Время размещения')
    bot.send_message(message.chat.id, 'Вводи юзернейм, как введешь - жми Время размещения',
                     reply_markup=keyboard)

@bot.message_handler(func= lambda message: message.text == 'Время размещения', content_types=['text'])
def username(message):
    keyboard = types.ReplyKeyboardMarkup(True, )
    keyboard.row('Готово')
    bot.send_message(message.chat.id, 'Пиши время в виде 2/24 где 2 - время в топе, 24 - общее время',
                     reply_markup=keyboard)

@bot.message_handler(func= lambda message: message.text == 'Готово', content_types=['text'])
def done(message):
    bot.send_message(message.chat.id, 'Отлично, можешь вернуться',
                     reply_markup=keyboard_back_to_start())

@bot.message_handler(func= lambda message: message.text == 'Назад', content_types=['text'])
def back(message):
    bot.send_message(message.chat.id, 'Кем будешь?', reply_markup=keyboard_start())

@bot.message_handler(func= lambda message: message.text == 'Смотреть заявки', content_types=['text'])
def see_orders(message):
    bot.send_message(message.chat.id, 'Пока не работает', reply_markup=keyboard_back_to_start())

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
