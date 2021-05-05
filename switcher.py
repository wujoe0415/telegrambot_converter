from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot ,Message
from youtube_dl.postprocessor.ffmpeg import FFmpegMetadataPP

import youtube_dl as yt
import json
import os
import logging

import mutagen

import mutagen.mp3
from mutagen.id3 import ID3, ID3NoHeaderError, TPE1
from mutagen.easyid3 import EasyID3


# import telebot
#from telebot import types

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)
vlink = " " 
new_name = " " 
artist_name = " " 



def artname(update: Update, context: CallbackContext):
    global artist_name
    artist_name = update.message.text[:].replace('\n', '')
    

def reform(update: Update, context: CallbackContext):
    #updater = Updater('1682027455:AAGriDdVHTH37BnzFCxP4zBFt1ADWv17JgI', use_context=True)

    global new_name
    # update.message.reply_text(update.message.chat.username + ",please enter the song title.")
    new_name = update.message.text[8:].replace('\n', '')
    #update.message.reply_text(update.message.chat.username + ",please enter the song title.")
    #updater.dispatcher.add_handler(MessageHandler(Filters.text,rename))
    #context.bot.register_next_step_handler(Filters.text,rename)



    update.message.reply_text(update.message.chat.username + ",please enter the artist\'s name.")
    #updater.dispatcher.add_handler(MessageHandler(Filters.text,artname))
    #context.bot.register_next_step_handler(Filters.text,artname)

    # update.message.reply_text(update.message.chat.username + ",please enter the artist name.")
    

def link(update: Update, context: CallbackContext):
    global vlink
    vlink = update.message.text[6:].replace('\n', ' ')

def start(update: Update, context: CallbackContext):
# def start(bot,update):

    # update.message.reply_text(text='Example')

    update.message.reply_text('Welcome to use this converter, '+ update.message.chat.username +", please type \\converter ")
    # .message.from_user_name == update.message.text.name

    
def end(update: Update, context: CallbackContext):
    global vlink, new_name
    vlink = ' '
    new_name = ' '
    update.message.reply_text(update.message.chat.username + ", thanks you!")

    # updater.dispatcher.add_handler

def convert(update: Update, context: CallbackContext):
    global vlink, new_name,artist_name
    #update.message.reply_text(update.message.chat.username +', 請貼上影片的網址(輸入'+'/'+'end來取消)')
    #update.message.reply_text(update.message.chat.username+', 輸入你想要的檔案名稱(輸入'+'/'+'end來取消)')
   
    
    ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': new_name +'.mp3',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'
                }]
            }
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(vlink, download=False)
            
            ydl.download([vlink])
            
            #ydl.add_post_processor(FFmpegMetadataPP(metadata))
            #video_title = info_dict('title',vlink)
    
    except Exception:
        context.bot.send_message(chat_id=update.message.chat_id,text="Sorry, I can't find this video, please check about the link you pasted again.")
        new_name = ' '
        vlink=' '
        return False
        
        # break this function
   

    #os.rename(video_title+".map3",new_name+".mp3")
    
    filenam = new_name +".mp3"

    try:
        #audioo = ID3(filenam)
        audioo =ID3()
        #audioo = EasyID3()
        audioo.save(filenam)

    except mutagen.id3.ID3NoHeaderError:
        audioo = ID3()
        audioo.load(filenam)#filename, easy=True)
        #audioo.add_tags()
    #type(audioo)
    #audioo['artist'] = mutagen.id3.TextFrame(encoding=3, text=artist_name)#artname
    #audioo['TPE1'] = mutagen.id3.TextFrame(encoding=3, text=artist_name)
    audioo['TPE1'] = TPE1(encoding=3, text=artist_name)
    audioo.save(filenam,v2_version=3)

    formats = info_dict['formats']
    #formats is a list of dictionaries, pick the format you are looking for
    format = formats[0]
    
    
    if(format['filesize'] > 50000000):
        update.message.reply_text(update.message.chat.username,",sorry! This file seems to be too heavy")
    else :
        #update.message.reply_text(update.message.chat.username,new_name+".mp3") 
        context.bot.sendAudio(chat_id=update.message.chat_id,audio = open(new_name+'.mp3', 'rb'))

    
    #"new_name.mp3" == audio=open(info_dict.get('title', info_dict.get('title', 'video')

    #os.remove(new_name+".mp3")
    new_name = ' '
    vlink=' '

def main():
    updater = Updater('1682027455:AAGriDdVHTH37BnzFCxP4zBFt1ADWv17JgI', use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("convert", convert, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("reform", reform))
    updater.dispatcher.add_handler(CommandHandler("link", link))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, artname))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()