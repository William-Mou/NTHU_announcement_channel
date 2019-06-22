NTHU Announcement Channel
===

## Table of Contents

* NTHU Announcement Channel
  * Table of Contents
  * Beginners Guide
  * server flows
  * Appendix and FAQ
  
## Beginners Guide

If you are a total beginner to this, start here!

1. 下載此專案至你的電腦
```shell
git clone https://github.com/William-Mou/NTHU_announcement_channel.git
```
2. 進入專案資料夾，並設置你的 TOKEN 為環境變數
```shell
cd NTHU_announcement_channel && export TLELPOT_TOKEN='your_Telegram_bot_TOKEN'
```
3. Docker-compose 指令，自動部署 db 與 python 程式
``` shell
docker-compose up --build --remove-orphans --abort-on-container-exit
```



server flows
---
```sequence
python -> MySQL: 查詢公告已儲存？
Note right of MySQL: 如果未儲存
MySQL -> python: 回覆公告不存在
Note left of python: 推播 TG Channel
python -> MySQL: 儲存當筆新公告
```

## Appendix and FAQ

:::info
**Find this document incomplete?** Leave a issue!
:::

###### tags: `Telegram` `NTHU`
