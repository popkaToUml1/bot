import telebot
from telebot import types 
bot = telebot.TeleBot("8498799772:AAFLYxXACnN1x2o4efZsM7sFUjuJi55g-XI")

@bot.message_handler(commands=["start"])
def start(message):
    video = open("/media/intro.mp4", 'rb')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Чьо такое бот?")
    button2 = types.KeyboardButton("Как создать бота?")
    button3 = types.KeyboardButton("Кнопки")
    button4 = types.KeyboardButton("Медиа")
    button5 = types.KeyboardButton("Полезные ссылки")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_video_note(message.chat.id, video, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == "Чьо такое бот?":
        photo = open('media/media/kot.jpg', 'rb')
        inline_markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Документация", url="https://pytba.readthedocs.io/ru/latest/index.html")
        btn2 = types.InlineKeyboardButton("Википедия", url="https://ru.wikipedia.org")
        inline_markup.add(btn1,btn2)
        bot.send_photo(message.chat.id, photo, caption="Telegram-бот-это программа , которая работает внутри мессенжера.", reply_markup=inline_markup)

    elif  message.text == "Кнопки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("ДА")
        button2 = types.KeyboardButton("нет")
        button3 = types.KeyboardButton("Не Зна.")
        markup.add(button1,button2,button3)
        bot.send_message(message.chat.id, "Reply-клавиатура -заменяет обычную клавиатуру внизу экрана" "Нажмите на одну из кнопок", reply_markup=markup)

bot.polling(none_stop=True)
