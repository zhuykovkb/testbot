import datetime

import telebot

import config

print("Starting at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

bot = telebot.TeleBot(config.token)


def log(message, answer):
    print("\n ::::::::::")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2})\nТекст - {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer)


@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "Helloooo, how are you doing?")


@bot.message_handler(commands=['snail'])
def send_welcome(message):
    if message.from_user.id == 213701955:
        bot.reply_to(message, "I love u!!!! My little snail")
    log(message, '')


@bot.message_handler(commands=['register'])
def check(message):
    log(message, '')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = "Now i don't know how i can help u:("
    bot.reply_to(message, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
