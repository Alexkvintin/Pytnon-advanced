from telebot import TeleBot
from telebot.types import *
from config import TOKEN
import DBCM

user_id = None
bot = TeleBot(TOKEN)
phone = 'None'
fullname = None
surname = None
patronymic = None
mail = None
addition = ''
db = "bot.db"



@bot.message_handler(content_types=['text'])
def start(message):
    global user_id
    user_id = message.chat.id
    if message.text == '/reg':
        bot.send_message(message.chat.id, "Как вас зовут ?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.chat.id, 'Напишите /reg')


def get_name(message):
    global fullname
    fullname = message.text
    bot.send_message(message.chat.id, 'Введите фамилию ?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, 'Введите отчество ?')
    bot.register_next_step_handler(message, get_patronymic)


def get_patronymic(message):
    global patronymic
    patronymic = message.text
    bot.send_message(message.chat.id, 'Введите вашу почту: ')
    bot.register_next_step_handler(message, get_mail)


def get_mail(message):
    global mail
    mail = message.text
    bot.send_message(message.chat.id, 'Введите номер телефона: ')
    bot.register_next_step_handler(message, get_phone)


def get_phone(message):
    global phone
    if len(message.text) == 12:
        try:
            phone = int(message.text)
            bot.send_message(message.chat.id, 'Будут пожелания ?')
            bot.register_next_step_handler(message, get_addition)
        except ValueError:
            bot.send_message(message.chat.id, 'Номер телефона введен не коректно !\nНомер должен содержать 12 цифр\nВведие номер телефона в формате \'380xxxxxxxхх\'')
            bot.register_next_step_handler(message, get_phone)
    else:
        bot.send_message(message.chat.id,
                         'Номер телефона введен не коректно !\nНомер должен содержать 12 цифр\nВведие номер телефона в формате \'380xxxxxxxхх\'')
        bot.register_next_step_handler(message, get_phone)


def get_addition(message):
    global addition
    addition = message.text
    kb = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='Да', callback_data='yes')
    button2 = InlineKeyboardButton(text='Нет', callback_data='no')
    kb.add(button1, button2)
    question = f'Ваш номер телефона {phone}, Вас зовут {fullname} {surname} {patronymic}, пожелания: {addition} ?'
    bot.send_message(message.from_user.id, text=question, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        with DBCM.ContextManager(db) as cursor:
            info = "insert into users('user_id', 'fullname', 'surname', 'patronymic', 'mail', 'phone', 'additionally') values(?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(info, [user_id, fullname, surname, patronymic, mail, phone, addition])
        bot.send_message(call.message.chat.id, 'Отлично !')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Напишите /reg')


if __name__ == '__main__':
    bot.polling(none_stop=True)
