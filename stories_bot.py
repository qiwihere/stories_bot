import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

token = '656422356:AAH37sT-yMZnDEGKtEdgtoX27OHVsl-sT-4'

updater = Updater(token=token)
dispatcher = updater.dispatcher


def start(bot, update):
    custom_keyboard = [['top-left', 'top-right'],
                       ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)



updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
