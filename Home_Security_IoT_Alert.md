# Home_Security_IoT_Alert

Home_Security_IoT_Alert是一個以樹莓派為中心,利用webhook接收HTTP請求,由webhook傳送e-mail通知用戶,達到居家安全警報的作用.

# 已知bug!

  - 程式碼post請求的部份已經拿掉key,因此如果要使用webhook的功能需要先去IFTTT上註冊,設定e-mail,取得你專屬的key


### 技術

* [樹莓派] -使用樹莓派接收感測器的數值
* [webhook](https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook) - Handling raspberry pie http requests by webhook


###所需硬體
  - 一個樹莓派
  - 16GB SD CARD
  - 一個PIR感測器
  - 一個蜂鳴器
  - 一個火焰感測器
  - 兩個KY024感測器
  - MCP3008 一個
  - AIR QUALITY感測器一個
  - USB電源線
  - 色碼電阻 100 歐姆
  - 杜邦線

###使用的模組
  - spidev-spi接腳的模組
  - time-時間模組
  - GPIO-GPIO接腳的模組
  - os-系統的模組
  - requests-HTTP的模組

