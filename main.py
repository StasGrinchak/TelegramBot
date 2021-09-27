#2043444702:AAEXY9_kT90nK1PmlTs0Y_IYpbBC6v-LgKg

import telebot
from telebot import types
import datetime
from datetime import datetime


token = '2043444702:AAEXY9_kT90nK1PmlTs0Y_IYpbBC6v-LgKg'
bot=telebot.TeleBot(token)
#=====================================================

#=====================================================

@bot.message_handler(commands=['start'])
def startTextBot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Я тут')
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! \nЯ {1.first_name}. '.format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)
    user = message.from_user.username

@bot.message_handler(commands=['stop'])
def start(message):
    chats = 674868256
    bot.send_message(chat_id=chats, text="tests /end")
    return chats

@bot.message_handler(commands=['end'])
def start(message):
    chats = 674868256
    bot.send_message(chat_id=chats, text="tests /stop")



@bot.message_handler(content_types=['text'])
def startTextBot(message):
    hourMinute = datetime.now()
    print(hourMinute.minute)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('⏲ Да я таймер запустил')
    bot.send_message(message.chat.id, "Ты таймер запустил ?", reply_markup=markup)
    print(message.chat.id)

    if message.text == "⏲ Да я таймер запустил":
        # Запуск скрипта на изменения статуса
        chats =674868256
        bot.send_message(chat_id=chats,  text="tests")
        flag=False


def morning():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('⏲ Да я таймер запустил')
    chats = 674868256
    bot.send_message(chat_id=chats, text="Ты таймер запустил ?",reply_markup=markup)

#morning()

bot.polling(none_stop=False)



#     hourMinute = datetime.now()
#     nowday = datetime.today().strftime('%A')
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#     hour = [9,14,17]
#     minus = [10,15,20,25,30,35,40,45,50,55]
#     if nowday in days:
#         print("days OK")
#         if hourMinute.hour in hour:
#             print("hour ok")
#             flag=True
#bots.polling(none_stop=True)
#
#

#
