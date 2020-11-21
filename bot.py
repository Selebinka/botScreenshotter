import os

import telebot
import validators

import config
from utils import get_screenshot_from_page

bot = telebot.TeleBot(config.TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def hello_user(message):
    """Return message with 'Hello, {username}!' """
    bot.send_message(message.chat.id, 'Hello, {}!'.format(
                                                message.from_user.username))


@bot.message_handler(commands=['help'])
def show_help(message):
    """Return help message"""
    bot.send_message(message.chat.id, 'To get screenshot of webpage use command /getscreenshot.\
                                       For example: /getscreenshot https://www.google.com')


@bot.message_handler(commands=['getscreenshot'])
def get_screenshot(message):
    """Send page screenshot from link"""
    uid = message.chat.id
    try:
        url = message.text.split(' ')[1]

        if not validators.url(url):
            bot.send_message(uid, 'Incorrect URL!')
        else:
            screenshot_path = '{}.png'.format(uid)
            get_screenshot_from_page(
                                url=url,
                                screenshot_path=screenshot_path
                                )
            try:
                bot.send_photo(uid, photo=open(screenshot_path, 'rb'))
            except Exception:
                bot.send_document(uid, data=open(screenshot_path, 'rb'))

        os.remove(screenshot_path)

    except IndexError:
        bot.send_message(uid, 'You have not entered URL!')
        return
    

if __name__ == '__main__':
    bot.infinity_polling()
