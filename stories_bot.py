import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

token = '656422356:AAH37sT-yMZnDEGKtEdgtoX27OHVsl-sT-4'

updater = Updater(token=token)
dispatcher = updater.dispatcher

default_keyboard = [
    ['Случайная история'],
    ['По категориям'],
    ['О боте']
]

categories = json.loads(requests.get('https://storiesapi.herokuapp.com/', params={'type': 'stories',
                                                                       'action': 'categories'}).content)['categories'].values()

categories_keyboard = [['Назад']]
k = 0
line = []
cols = 3
for category in categories:
    k += 1
    line.append(category)

    if not k % cols:
        categories_keyboard.append(line)
        line = []

categories_keyboard.reverse()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Выбери подходящий запрос',
                     reply_markup=ReplyKeyboardMarkup(default_keyboard))


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
            stories = response['data']
            bot.send_message(chat_id=update.message.chat_id,
                             text=('via: %s\n\n%s' % (via, stories)))

    if update.message.text == 'Назад':
        bot.send_message(chat_id=update.message.chat_id,
                         text='Главное меню',
                         reply_markup=ReplyKeyboardMarkup(default_keyboard))

    if update.message.text == 'По категориям':
        bot.send_message(chat_id=update.message.chat_id,
                         text='Категории',
                         reply_markup=ReplyKeyboardMarkup(categories_keyboard))

    if update.message.text in categories:
        params = {
            'type': 'stories',
            'action': 'by_cat',
            'tag': update.message.text
        }
        r = requests.get('https://storiesapi.herokuapp.com/', params=params)
        if r.content:
            response = json.loads(r.content)
            via = response['via']
            stories = response['data']
            bot.send_message(chat_id=update.message.chat_id,
                             text=('via: %s\n\n%s' % (via, stories)))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text_message))
updater.start_polling()
