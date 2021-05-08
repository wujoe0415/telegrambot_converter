# telegrambot_converter
專案為 telegram bot ，可以將 youtube 影片之音訊檔（ mp3檔 ）以想要的格式轉換並回傳使用者。
但尚未完成
## 指令介紹
+ /start : 介紹怎麼用這個bot
+ /end : 謝謝
+ /convert : 轉換指令
+ /reform + 一個空格 + 檔名（ 不須加.mp3 ）: 更改格式
+ /link + 一個空格 + 連結（ 限定 youtube 連結，yt影片按分享後複製該連結 ): 你希望轉換之影片網址
+ 純訊息 : artist 名字

## 運用函式
+ youtube_dl : 搜尋接收之 youtube 連結，並下載至伺服器 
+ mutagen : 更改 mp3 檔格式，例如 title 、artist、album、year等等 

## 目前的 bug
+ telegram bot 傳送之 mp3檔別地無法聽，但本地可以
+ mutagen 的格式可能有誤，有更改的程式碼卻沒有更改（有時傳送之 mp3 檔可以看到 artist name 但在本地端的 properties 卻顯示 unknown 

