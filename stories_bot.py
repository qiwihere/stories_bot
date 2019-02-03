import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

token = '656422356:AAH37sT-yMZnDEGKtEdgtoX27OHVsl-sT-4'

updater = Updater(token=token)
dispatcher = updater.dispatcher


want_more_keyboard = [
    ['Ещё'],
    ['Назад']
]


def start(bot, update):
    default_keyboard = [
        ['Случайная история'],
        ['По категориям'],
        ['О боте']
    ]

    bot.send_message(chat_id=update.message.chat_id,
                     reply_markup=ReplyKeyboardMarkup(default_keyboard))

'''
def text_message(bot, update):
    if update.message.text == 'Случайная история' or update.message.text == 'Ещё':
        params = {
            'type': 'stories',
            'action': 'random'
        }
        r = requests.get('https://storiesapi.herokuapp.com/', params=params)
        if r.content:
            response = json.loads(r.content)
            via = response['via']
            stories = response['stories']
            bot.send_message(chat_id=update.message.chat_id,
                             text=('via: %s\n\n%s' % (via, stories)),
                             reply_markup=ReplyKeyboardMarkup(want_more_keyboard))

'''
updater.dispatcher.add_handler(CommandHandler('start', start))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, text_message))
updater.start_polling()
