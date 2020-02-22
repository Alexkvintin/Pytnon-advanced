from telebot import *
from config import TOKEN
from keyboard import *
from models import models
from telebot.types import *

STORE_NAME = "TELEMAGAZ"
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # получаем параметр "info" элемента БД по заданому параметру "title"
    greeting = models.Texts.objects(title='Greetings').get().info
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*kb.values())
    bot.send_message(message.chat.id, greeting, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def main_text_handler(message):
    if message.text.lower() == 'информация о магазине':
        # Так же как и в "start"
        about = models.Texts.objects(title='About').get().info
        bot.send_message(message.chat.id, about)
        return

    elif message.text.lower() == 'последние новости':
        # Так же как и в "start"
        news = models.Texts.objects(title='Last news').get().info
        bot.send_message(message.chat.id, news)
        return

    elif message.text.lower() == 'продукты':
        keyboard = InlineKeyboardMarkup(row_width=1)
        # Получаем объекты класса "Category" с БД, записываем их "title" в кнопки
        keyboard.add(*[InlineKeyboardButton(i.title, callback_data='category_' + str(i.id)) for i in models.Category.get_root_categories()])
        bot.send_message(message.chat.id, "Выберите категорию", reply_markup=keyboard)

    elif message.text.lower() == 'продукты со скидкой':
        # Получаем объекты класса "Product" с установленным параметром "is_discount" в "True"
        product = models.Product.objects(is_discount=True)
        for i in product:
            photo = i.photo.read()
            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton(text='Добавить в корзину', callback_data='add-to-cart_' + str(i.id)))
            bot.send_photo(message.chat.id, photo, parse_mode='HTML', caption=f"<b>{i.title}</b>\nСтарая цена: " + str(i.price) + 'грн.' + "\n<b>Новая цена:" + str(i.new_price) + 'грн.' + "</b>" + f"\n{i.description}", reply_markup=keyboard)

    elif message.text.lower() == 'корзина':
        # Проверяем на соответствие "user_id" с id чата
        if message.chat.id in models.User.objects.distinct("user_id"):
            # Получаем объект класса "User" с БД, по id в телеграме
            user = models.User.objects.get(user_id=message.from_user.id)
            # Получаем объект класса "Cart" с БД, по заданым параметрам
            user_cart = models.Cart.objects(user=user, active=True)
            if not user_cart:
                bot.send_message(message.chat.id, "Корзина пуста")
                return
            cart_sum_now = 0
            cart_text = ""
            for i in user_cart:
                cart_text = cart_text + i.product.title + " " + str(i.product.get_price) + " грн.\n"
                cart_sum_now += i.product.get_price
            cart_sum = models.Cart().get_cart_sum(user)
            cart_text = "Сума товаров в корзине: " + str(cart_sum_now) + " грн." + "\n" + cart_text + "Общая сумма покупок: " + str(cart_sum) + " грн."
            keyboard = InlineKeyboardMarkup()
            keyboard.add(*[
                InlineKeyboardButton(text='Купить', callback_data='by-cart_' + str(i.user.id)),
                InlineKeyboardButton(text='Очистить корзину', callback_data='clear-cart_' + str(i.user.id))])
            bot.send_message(message.chat.id, cart_text, reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'Корзина пуста')
    else:
        pass


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_products_or_subcategory(call):
    _id = call.data.split("_")[1]
    # Получаем объект класса "Category" с БД, по заданому id
    category = models.Category.objects(id=_id).get()
    if category.is_parent:
        keyboard = InlineKeyboardMarkup(row_width=2)
        # Получаем все "subcategory" объекта, записываем их "title" в кнопки
        keyboard.add(*[InlineKeyboardButton(i.title, callback_data='category_' + str(i.id)) for i in category.subcategory],
                     InlineKeyboardButton(text="<<", callback_data=f'back_{category.id}'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что будем брать ?", reply_markup=keyboard)
    else:
        # Если проверка на родительскую категорию не была прйдена, возвращаем объекты класса "Product", что принадлежат текущей категории
        product = category.get_products()
        for i in product:
            photo = i.photo.read()
            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton(text='Добавить в корзину', callback_data='add-to-cart_' + str(i.id)))
            if i.is_discount:
                bot.send_photo(call.message.chat.id, photo, parse_mode='HTML', caption=f"<b>{i.title}</b>\nСтарая цена: " + str(i.price) + "\n<b>Новая цена:" + str(i.new_price) + "</b>" + f"\n{i.description}", reply_markup=keyboard )
            else:
                bot.send_photo(call.message.chat.id, photo, parse_mode='HTML', caption=f"<b>{i.title}</b>\n<b>Цена: " + str(i.price) + "</b>" + f"\n{i.description}", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add-to-cart')
def add_to_cart(call):
    if call.from_user.id not in models.User.objects.distinct("user_id"):
        user = models.User(**{"user_id": call.from_user.id}).save()
    else:
        user = models.User.objects.get(user_id=call.from_user.id)
    product = models.Product.objects.get(id=call.data.split('_')[1])
    models.Cart(**{"user": user, "product": product}).save()
    bot.send_message(call.message.chat.id, "Товар " + product.title + " добавлен в корзину")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'clear-cart')
def clear_cart(call):
    models.Cart.objects(active=True, user=call.data.split('_')[1]).delete()
    bot.send_message(call.message.chat.id, "Корзина очищена")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'by-cart')
def by_cart(call):
    cart = models.Cart.objects(active=True, user=call.data.split('_')[1])
    for i in cart:
        models.OrderHistory(**{"cart": i}).save()
    cart.update(active=False)
    bot.send_message(call.message.chat.id, "Спасибо за покупку!")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'back')
def go_back(call):
    _id = call.data.split("_")[1]
    category = models.Category.objects(id=_id).get()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*[InlineKeyboardButton(i.title, callback_data='category_' + str(i.id)) for i in category.get_root_categories()])
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите категорию', reply_markup=keyboard)


if __name__ == "__main__":
    print("started")
    bot.polling(none_stop=True)
