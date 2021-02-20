from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot 

import youtube_dl as yt
import json
import os
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)
link = ' '

def start(update: Update, context: CallbackContext):
# def start(bot,update):

    # update.message.reply_text(text='Example')

    update.message.reply_text('Welcome to use this converter, '+ update.message.chat.username +" , please type \\converter ")
    # .message.from_user_name == update.message.text.name

    
def end(update: Update, context: CallbackContext):
    link = ' '
    new_name = ' '
    update.message.reply_text(update.message.chat.username + ", thanks you!")

    # updater.dispatcher.add_handler
    

def convert(bot,update: Update):
    
    update.message.reply_text(update.message.chat.username+', 請貼上影片的網址(輸入'+'/'+'end來取消)')
    link = update.message.text
    update.message.reply_text(update.message.chat.username+', 輸入你想要的檔案名稱(輸入'+'/'+'end來取消)')
    new_name = update.message.text 
    
    ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': link +'.mp3',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'
                }]
            }
    
    with yt.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        ydl.download([link])
        video_title = info_dict('title',link)

    os.rename(video_title+".map3",new_name+".mp3")
    
    new_name = ' '
    link=' '
    
    if(info_dict.get('size',link) > 50000000):
        bot.sendMessage(update.message.chat.username,",sorry! This file seems to be too heavy")
    else :
        bot.sendAudio(update.message.chat.username,new_name+".mp3") 

    #"new_name.mp3" == audio=open(info_dict.get('title', info_dict.get('title', 'video')

    os.remove(new_name+".mp3")
def main():
    updater = Updater('1682027455:AAGriDdVHTH37BnzFCxP4zBFt1ADWv17JgI', use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("convert", convert))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()