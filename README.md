# Home_Security_IoT_Alert
Home_Security_IoT_Alert是一個以樹莓派為中心,利用webhook接收HTTP請求,由webhook傳送e-mail通知用戶,達到居家安全警報的專題.
# 功能 Features!
* 室內火焰偵測警報
* 室內氣體偵測警報
* 門窗感測防盜警報
* 浴室防滑警報
* 警報日誌
* 即時email通知
* 腳本運行

# 已知bug!
  - 程式碼post請求的部份已經拿掉key,因此要使用webhook的功能需要先去IFTTT上註冊,設定e-mail,取得你專屬的key
### 技術
* [webhook](https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook) - 註冊並填寫信箱帳號及預設email警報內容，取得專屬http url，並添加進程式碼
* [RUN A SCRIPT AS A SERVICE IN RASPBERRY PI](http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/?fbclid=IwAR0WYwCgxtz1eEy-FjbpWr50aqoabVS2MkNYJ4UrLyqSpqFt-rRdiXUY9tc)- 在沒有螢幕的情況下,背景執行
* python
* Raspberry Pi

### 所需硬體

  - 一個樹莓派
  - 一個16GB SD CARD
  - 一個PIR感測器
  - 一個蜂鳴器
  - 一個火焰感測器
  - 兩個KY024感測器
  - 一個MCP3008
  - 一個AIR QUALITY感測器
  - USB電源線
  - 一個100歐姆色碼電阻
  - 杜邦線
  

### requirements install
```sh
$    pip install -r requirements.txt
```

### 待辦事項 Todos

#### 參考資源 Reference resource
[Raspberry Pi](https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp)