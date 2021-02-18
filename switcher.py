from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import youtube_dl
import json
import os

def convert(bot,update):
    bot.sendMessage('welcome to use this converter,',update.message.from_user_name,'please paste on the youtube video link.')


def start(bot,update):
    bot.sendMessage('welcome to use this converter,',update.message.from_user_name,'please paste on the youtube video link.')

def end(bot,update):
    link = ''
    bot.sendMessage(update.message.from_user_name, "thanks you!")

updater = Updater('1682027455:AAGriDdVHTH37BnzFCxP4zBFt1ADWv17JgI')
updater.dispatcher.add_handler(MessageHandler(Filters.video, convert))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("end", end))
updater.start_polling()
updater.idle()