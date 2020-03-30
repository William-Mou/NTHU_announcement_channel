NTHU Announcement Channel
===

> For Django

## Table of Contents

* NTHU Announcement Channel
  * Table of Contents
  * Beginners Guide
  * To Developers
  * Appendix and FAQ
  
## Beginners Guide

If you are a total beginner to this, start here!

1. 下載此專案至你的電腦
```shell
git clone https://github.com/William-Mou/NTHU_announcement_channel.git
```
2. 進入專案資料夾，並設置你的 TOKEN 為環境變數
```shell
cd NTHU_announcement_channel && export TELEPOT_TOKEN='your_Telegram_bot_TOKEN'
```
3. Docker-compose 指令，自動部署 db 與 python 程式
``` shell
docker-compose up --build --remove-orphans --abort-on-container-exit
```

## To Developers
---

### Server Flows

![](https://i.imgur.com/FzozhTL.png)

### Project Tree

```
.
├── README.md
├── docker  (what container or image need )
│   ├── mysql   (mysql container volumed file)
│   │   └── data
│   │       ├── db   (database)
│   │       └── conf
│   └── tgchannel   (building pythob image needed)
│       ├── crawler   (University announcement crawler.py)
│       │   ├── NTHU_CS.py
│       │   ├── NTHU_EE.py
│       │   ├── NTHU_IPTH.py
│       │   ├── modules
│       │   │   ├── TGMySQL.py
│       │   │   ├── __init__.py
│       │   │   └── __pycache__
│       │   │       ├── TGMySQL.cpython-36.pyc
│       │   │       └── __init__.cpython-36.pyc
│       │   ├── not_in_used
│       │   │   └── nthu_ipth.py
│       │   └── resource   (University announcement link.json)
│       │       ├── nthu_cs.json
│       │       ├── nthu_ee.json
│       │       └── nthu_ipth.json
│       ├── dockerfile
│       ├── requirements.txt
│       └── run.py   (excute all crawler.py when docker run container)
├── docker-compose.yml
├── jupyter_notebook_test   (test some new features (like my playground) )
│   ├── nthu_cs.ipynb
│   └── nthu_ee_cs.json
├── todo_list.md
└── tree   (this graphic)
```

### If you want to write something...

1. Make your target_links as a json file, and put it down ```docker/tgchannel/crawler/resource``` folder.

2. Writing a ```SCHOOL_DEPARTMENT.py``` , you could import SQL functions by ```from modules import TGMySQL```.

3. Just that, have fun ! Pull requests are welcome 🙏 ~

## Appendix and FAQ

:::info
**Find this document incomplete?** Leave a issue!
:::

###### tags: `Telegram` `NTHU`
