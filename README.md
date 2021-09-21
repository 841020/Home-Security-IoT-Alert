# smart_home

- Develop and deploy server on Raspberry Pi.
- The sensor sends an analog signal through the gpio pin.
- ADC (Analogue-to-digital converter) sends the processed signal to the server.
- The server performs corresponding follow-up actions according to the value.
- Publish new triggers or actions by Webhooks api on IFTTT

# 功能 Features!

- 室內火焰偵測警報
- 室內氣體偵測警報
- 門窗感測防盜警報
- 浴室防滑警報
- 警報日誌
- 即時 email 訂閱通知

### 技術

- [webhook](https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook) - 註冊帳號並預設 email 及警報內容，取得專屬 url key，將 HTTP Request 加上 url key
- [RUN A SCRIPT AS A SERVICE IN RASPBERRY PI](http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/?fbclid=IwAR0WYwCgxtz1eEy-FjbpWr50aqoabVS2MkNYJ4UrLyqSpqFt-rRdiXUY9tc) - 腳本運行
- Python3
- Raspberry Pi 3
- HTTP

### 所需硬體

- 一個樹莓派
- 一個 16GB SD CARD
- 一個 PIR 感測器
- 一個蜂鳴器
- 一個火焰感測器
- 兩個 KY024 感測器
- 一個 MCP3008
- 一個 AIR QUALITY 感測器
- USB 電源線
- 一個 100 歐姆色碼電阻
- 杜邦線

### requirements install

```sh
$    pip install -r requirements.txt
```

#### 參考資源 Reference resource

[Raspberry Pi](https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp)
[ADC reference](https://atceiling.blogspot.com/2014/04/raspberry-pi-mcp3008.html)
