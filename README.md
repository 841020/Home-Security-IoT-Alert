# smart_home

- smart home 使用樹莓派,連接感測器收集資料,使用 webhook api 發送電子郵件通知訂閱用戶,實現居家安全監控。

- Smart home uses a Raspberry Pi, connects to sensors to collect data,<br>
  and uses webhook api to send emails to notify subscribers to achieve home security monitoring.

# 功能 Features!

- 腳本運行
- 室內火焰偵測警報
- 室內氣體偵測警報
- 門窗感測防盜警報
- 浴室防滑警報
- 警報日誌
- 即時 email 訂閱通知

### 技術

- [webhook](https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook) - 註冊帳號並預設 email 及警報內容，取得專屬 url key，並添加 http request
- [RUN A SCRIPT AS A SERVICE IN RASPBERRY PI](http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/?fbclid=IwAR0WYwCgxtz1eEy-FjbpWr50aqoabVS2MkNYJ4UrLyqSpqFt-rRdiXUY9tc) - 腳本運行
- Python3
- Raspberry Pi
- HTTP POST

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
