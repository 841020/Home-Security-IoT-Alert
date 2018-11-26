# Home_Security_IoT_Alert
Home_Security_IoT_Alert是一個以樹莓派為中心,利用webhook接收HTTP請求,由webhook傳送e-mail通知用戶,達到居家安全警報的專題.

# 已知bug!

  - 程式碼post請求的部份已經拿掉key,因此要使用webhook的功能需要先去IFTTT上註冊,設定e-mail,取得你專屬的key


### 技術

* [webhook](https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook) - 接收樹莓派HTTP請求,並設定e-mail接收預設的警報訊息
* [RUN A SCRIPT AS A SERVICE IN RASPBERRY PI ](http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/?fbclid=IwAR0WYwCgxtz1eEy-FjbpWr50aqoabVS2MkNYJ4UrLyqSpqFt-rRdiXUY9tc)- 在沒有螢幕的情況下,背景執行
### 所需硬體

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

### 使用的模組

  - spidev-spi接腳的模組
  - time-時間模組
  - GPIO-GPIO接腳的模組
  - os-系統的模組
  - requests-HTTP的模組
  
