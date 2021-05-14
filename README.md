# telegrambot_converter
專案為 telegram bot ，可以將 youtube 影片之音訊檔（ mp3檔 ）以想要的格式轉換並回傳使用者。

## 安裝
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
## 指令介紹
+ /start : 介紹怎麼用這個bot
+ /end : 謝謝
+ /convert : 轉換指令
+ /reform + 一個空格 + 檔名（ 不須加.mp3 ）: 更改格式
+ /link + 一個空格 + 連結（ 限定 youtube 連結，yt影片按分享後複製該連結 ): 你希望轉換之影片網址
+ 純訊息 : artist 名字

## 運用函式
+ youtube_dl : 搜尋接收之 youtube 連結，並下載至伺服器 
+ mutagen : 更改 mp3 檔格式，例如 title 、artist 
