from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import youtube_dl as yt
import json
import os
link = ' '


def start(bot,update):
    bot.sendMessage('welcome to use this converter,',update.chat.username,'please paste on the youtube video link.')
    # .message.from_user_name == Chat.username
def end(bot,update):
    link = ' '
    new_name = ' '
    bot.sendMessage(update.message.from_user_name, "thanks you!")

    updater.dispatcher.add_handler
    

def convert(bot,update):
    

    link = update.message.text[5:].replace('\n',' ')
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
        info_dict = ydl.extract_info(link, download=False)
        ydl.download([link])
        video_title = info_dict('title',link)

    os.rename(video_title+".map3",new_name+".mp3")
    
    new_name = ' '
    link=' '
    
    if(info_dict.get('size',link) > 50000000):
        bot.sendMessage(update.message.from_user_name,",sorry! This file seems to be too heavy")
    else :
        bot.sendAudio(update.message.from_user_name,new_name+".mp3") 

    #"new_name.mp3" == audio=open(info_dict.get('title', info_dict.get('title', 'video')

    os.remove(new_name+".mp3")
updater = Updater('1682027455:AAGriDdVHTH37BnzFCxP4zBFt1ADWv17JgI')
updater.dispatcher.add_handler(MessageHandler(Filters.text, convert))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("end", end))
updater.start_polling()
updater.idle()