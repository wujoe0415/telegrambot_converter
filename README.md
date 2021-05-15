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
brew install youtube-dl
brew install ffmpeg
```
## Introduction
+ /start : iinstroduct bot
+ /end : Thanks for using~
+ /convert : start to convert
+ /reform + one space + filename（ don't add .mp3 ）: edit file info
+ /link + one space + link（ eg : https://youtu.be/... ): post the video link you want to convert 
+ only text : artist's name
## Instructions
![](https://i.imgur.com/imalkHq.png)


## About tis bot~
+ youtube_dl : search the youtube link, and download the mp3 file 
+ mutagen : edit mp3 format，eg : title 、artist 
