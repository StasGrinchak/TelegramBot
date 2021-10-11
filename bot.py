#2043444702:AAEXY9_kT90nK1PmlTs0Y_IYpbBC6v-LgKg
import os
from flask import Flask, request
import telebot
from telebot import types
from DB import *

#==========================================================================================================
server = Flask(__name__)
token = '2043444702:AAEXY9_kT90nK1PmlTs0Y_IYpbBC6v-LgKg'
bot=telebot.TeleBot(token)

#==========================================================================================================

@bot.message_handler(commands=['start'])# Создает в базе запись с ID чата
def startTextBot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('⏲ Да я запустил таймер с утра')
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! \nЯ {1.first_name}. '.format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)
    user_id = message.chat.id
    print(user_id)
    db  = DB()
    db.create_user(user_id)
#==========================================================================================================

@bot.message_handler(content_types=['text'])
def startTextBot(message):

    if message.text == "⏲ Да я запустил таймер с утра":
        # Запуск скрипта на изменения статуса
        chats =message.chat.id
        db_morning_update = DB()
        db_morning_update.morning_update(chats)
        bot.send_message(chat_id=chats,  text="morning_update")
        flag=False
    if message.text == "⏲ Да я запустил таймер вечером":
        # Запуск скрипта на изменения статуса
        chats =message.chat.id
        db_evening_update = DB()
        db_evening_update.evening_update(chats)
        bot.send_message(chat_id=chats,  text="evening_update")
        flag=False
#==========================================================================================================


def morning(): # Функция которая спрашивает у пользователя включтил ли он Таймер
    get_users_db = DB()
    for i in range(len(get_users_db.get_users())):
        if get_users_db.get_users()[i][1] == 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('⏲ Да я запустил таймер с утра')
            chats = get_users_db.get_users()[i][0]
            print(chats)
            try:
                bot.send_message(chat_id=chats, text="Ты таймер запустил ?",reply_markup=markup)
            except:
                print("Все плохо")
#==========================================================================================================

#morning()
def evening():
    get_users_db = DB()
    for i in range(len(get_users_db.get_users())):
        if get_users_db.get_users()[i][2] == 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('⏲ Да я запустил таймер вечером')
            chats = get_users_db.get_users()[i][0]
            try:
                bot.send_message(chat_id=chats, text="Ты таймер запустил ?", reply_markup=markup)
            except:
                print("Все плохо")
#==========================================================================================================

#evening()
def get_users_all_test_morning():
    get_users_db = DB()
    users_morning_statusF=[]
    for i in range(len(get_users_db.get_users())):
        if get_users_db.get_users()[i][1] == 1:
            print(get_users_db.get_users()[i][0])
            users_morning_statusF.append(get_users_db.get_users()[i][0])
    return users_morning_statusF
        #print(get_users_db.get_users()[i][1])
#==========================================================================================================

def mid_nigth_update():
    nigth_update=DB()
    nigth_update.mid_nigth_update()
mid_nigth_update()
#==========================================================================================================

#==========================================================================================================

@server.route('/' + token, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + token)
    return "!", 200
bot.polling(none_stop=True,interval=1)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
