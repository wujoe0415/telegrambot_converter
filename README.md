# Telegrambot_converter
This project is a Telegram bot ，and it is used for converting youtube video to a mp3 file.

## Installation
```shell
git clone https://github.com/wujoe0415/telegrambot_converter.git
cd telegrambot_converter
sudo apt install pipenv
pipenv install youtube_dl
pipenv install mutagen
pipenv install ffmpeg
brew python3
brew install youtube-dl
brew install ffmpeg
pipenv run python3 converter.py
```
## Introduction
+ /start : Instroduce bot
+ /end : Thanks for using~
+ /convert : Start to convert
+ /reform + one space + filename（ don't add .mp3 ）: Edit file info
+ /link + one space + link（ eg : https://youtu.be/... ): Post the video link you want to convert 
+ only text : Artist's name
## Instructions
![](https://i.imgur.com/imalkHq.png)


## About tis bot~
+ youtube_dl : searching the youtube link, and downloading the mp3 file 
+ mutagen : editing mp3 format，eg : title 、artist 
