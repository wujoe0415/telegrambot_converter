from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import youtube_dl as yt
import json
import os



def start(bot,update):
    bot.sendMessage('welcome to use this converter,',update.chat.username,'please paste on the youtube video link.')
    # .message.from_user_name == Chat.username
def end(bot,update):
    link = ''
    bot.sendMessage(update.message.from_user_name, "thanks you!")

    
    

def convert(bot,update):
    link = update.Filter.text
    bot.sendMessage(update.chat.username,'輸入你想要的檔案名稱(輸入'+'\\'+'end來取消)')
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
        ydl.download([link])

    os.rename(yt.__name__+".map3",new_name+".mp3")
    
    new_name = ''
    size = os.size(os.path(yt.__name__+".map3"))
    
    if(size > 50000000):
        bot.sendMessage(update.message.from_user_name,",sorry! This file seems to be too heavy")
    else :
        bot.sendAudio(update.message.from_user_name,audio=open(yt.title() + ".mp3",'rb'))

updater = Updater('1682027455:AAGriDdVHTH37BnzFCxP4zBFt1ADWv17JgI')
updater.dispatcher.add_handler(MessageHandler(Filters.text, convert))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("end", end))
updater.start_polling()
updater.idle()