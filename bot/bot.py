from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import random
bot = TeleBot('1063631487:AAGFi4YgRmkVcY-hR1BP4j02dTku7sEL9vc', threaded=False)


@bot.message_handler(commands=['start'])
def starting(message):
    print(message.chat.id)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    butt1 = KeyboardButton(text='Выбрать комплектующие')
    butt2 = KeyboardButton(text='Рандомноре число')
    butt3 = KeyboardButton(text='Собрать ПК')
    butt4 = KeyboardButton(text='Зайти в стим')
    kb.add(butt1, butt2, butt3, butt4)
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.chat.first_name} !', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Зайти в стим')
def steam(message):
    kr = InlineKeyboardMarkup(row_width=2)
    but1 = InlineKeyboardButton(callback_data='1', text='Главная', url='https://store.steampowered.com')
    but2 = InlineKeyboardButton(callback_data='2', text='Торговя площадка', url='https://steamcommunity.com/market/')
    but3 = InlineKeyboardButton(callback_data='3', text='Статистика', url='https://store.steampowered.com/stats/')
    but4 = InlineKeyboardButton(callback_data='4', text='Скидки', url='https://store.steampowered.com/specials')
    but5 = InlineKeyboardButton(callback_data='5', text='Чат', url='https://steamcommunity.com/chat/')
    kr.add(but1, but2, but3, but4, but5)
    bot.send_message(message.chat.id, 'Куда пойдём ?', reply_markup=kr)


@bot.message_handler(func=lambda message: message.text == 'Собрать ПК')
def build(message):
    bot.send_message(message.chat.id, 'https://telemart.ua/assembly.html')


@bot.message_handler(func=lambda message: message.text == 'Рандомноре число')
def rand(message):
    bot.send_message(message.chat.id, str(random.randint(1, 100)))


@bot.message_handler(func=lambda message: message.text == 'Выбрать комплектующие')
def hello(message):
    kb1 = InlineKeyboardMarkup(row_width=2)
    but1 = InlineKeyboardButton(callback_data='1', text='Материнские платы',url='https://ek.ua/k187.htm')
    but2 = InlineKeyboardButton(callback_data='2', text='Процессоры', url='https://ek.ua/k186.htm')
    but3 = InlineKeyboardButton(callback_data='3', text='Видеокарты', url='https://ek.ua/k189.htm')
    but4 = InlineKeyboardButton(callback_data='4', text='Блоки питания', url='https://ek.ua/k351.htm')
    but5 = InlineKeyboardButton(callback_data='5', text='Оперативная память', url='https://ek.ua/k188.htm')
    but6 = InlineKeyboardButton(callback_data='6', text='Жесткие диски', url='https://ek.ua/k190.htm')
    but7 = InlineKeyboardButton(callback_data='7', text='Ещё...')
    kb1.add(but1, but2, but3, but4, but5, but6, but7)
    bot.send_message(message.chat.id, 'Выберите комплектующие.', reply_markup=kb1)


@bot.callback_query_handler(func=lambda call: hello)
def callback(call):
    if call.message:
        if call.data == '7':
            hk = InlineKeyboardMarkup(row_width=2)
            but1 = InlineKeyboardButton(text='SSD', url='https://ek.ua/k61.htm')
            but2 = InlineKeyboardButton(text='Корпуса', url='https://ek.ua/k193.htm')
            but3 = InlineKeyboardButton(text='Системы охлаждения', url='https://ek.ua/k303.htm')
            but4 = InlineKeyboardButton(text='Звуковые карты', url='https://ek.ua/k192.htm')
            but5 = InlineKeyboardButton(text='Термопаста', url='https://ek.ua/k247.htm')
            hk.add(but1, but2, but3, but4, but5)
            bot.send_message(call.message.chat.id, 'Выберите комплектующие.', reply_markup=hk)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='переход...',
                              reply_markup=None)


@bot.message_handler(content_types=['text'])
def text(message):
    text = message.chat.text
    bot.send_message(message.chat.id, text=text)


if __name__ == '__main__':
    bot.infinity_polling(True)
