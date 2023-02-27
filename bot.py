import telebot
import config
from random import *
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
@bot.message_handler(commands=['start'])
def welcome(message):
    stik = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, stik)
    welcome_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    welcome_item1 = types.KeyboardButton("Привет!")
    welcome_markup.add(welcome_item1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}.\nМеня зовут <b>{1.first_name}</b>, и я не бот.\nПоздоровайся со мной!!!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=welcome_markup)

@bot.message_handler(content_types=['text'])
def say(message):
    if message.text == "Привет!" or message.text == "Назад!":
        bass_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bass_item1 = types.KeyboardButton("Рандомный режим")
        bass_item2 = types.KeyboardButton("Придумай пароль!")
        bass_item3 = types.KeyboardButton("Расскажи мне историю")
        bass_markup.add(bass_item1,bass_item2,bass_item3)
        bot.send_message(message.chat.id, "Привет, неуч.",parse_mode='html', reply_markup = bass_markup)
    #randommod
    elif message.text == "Рандомный режим":
        random_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        random_item1 = types.KeyboardButton("Рандомное число скажи!")
        random_item2 = types.KeyboardButton("Придумай пароль!")
        random_item3 = types.KeyboardButton("Назад!")
        random_markup.add(random_item1, random_item2, random_item3)
        bot.send_message(message.chat.id, "RANDOM MODE ACTIVATED", parse_mode='html', reply_markup=random_markup)
    elif message.text == "Рандомное число скажи!": bot.send_message(message.chat.id, "Хорошо, хорошо, ваше число - {}".format(randint(0, 100)))
    elif message.text == "Придумай пароль!": bot.send_message(message.chat.id, "Ваш пароль {}.\nНикому его не говорите!!!".format(f"{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}"))

    elif message.text == "Назад!": bot.send_message(message.chat.id, "Снова привет.",parse_mode='html', reply_markup = bass_markup)
    elif message.text == "Расскажи мне историю": bot.send_message(message.chat.id, "Нет(@_@)")
    else: bot.send_message(message.chat.id, "Я вас не понять.")
bot.polling(none_stop=True)
