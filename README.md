NTHU Announcement Channel
===

**!!Warning!! Alpha Version**

## issue

- some crawlers has problems.
- crawl command use dangerous eval, which could lead security issue.

  
## Beginners Guide

If you are a total beginner to this, start here!

```bash
#建立虛擬環境
python3 -m venv venv

#啓用虛擬環境
source venv/bin/activate

#安裝必要套件
pip install -r requirements.txt

#建立資料表
python3 manage.py migrate

#開始爬蟲
python3 manage.py crawl nthu
python3 manage.py crawl nctu

#查看資料
# 建議使用 DB Browser for SQLite 去檢視 `db.sqlite3` 這個檔案

#清空資料庫 table
python3 manage.py clean_tables News

```


## To Developers
---

### Server Flows

![](https://i.imgur.com/FzozhTL.png)


### If you want to write something...

1. Add school/department:
    - in `backend/` dir, please modify the `crawl.py`, `schools.py`, `url_list.py`.
2. Add new command:
    - in `backend/management/commands` dir, please add a new one.

## Appendix and FAQ

:::info
**Find this document incomplete?** Leave a issue!
:::

###### tags: `Telegram` `NTHU`
