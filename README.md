NTHU Announcement Channel
===

**Warning !** This is a Beta Version

此專案使用 Django 這個網頁框架來維護

## Issue

- some crawlers has problems.
  
## 環境建置

如果你對 Django 一竅不通，可以按照此操作完成環境建置。

```bash
# 建立虛擬環境
python3 -m venv venv

# 啓用虛擬環境
source venv/bin/activate

# 安裝必要套件
pip install -r requirements.txt

# 開發時建議安裝套件
pip install ipython

# 新增 .env 檔案
cp .env-example .env

# 建立資料表
python3 manage.py migrate

# 開始爬蟲
python3 manage.py crawl nthu
python3 manage.py crawl nctu

# 查看資料
# 可以使用 DB Browser for SQLite 去檢視 `db.sqlite3` 這個檔案
# 或是使用 DBeaver 去瀏覽

# 清空資料庫 table
python3 manage.py clean_tables News

# 傳送通知
python3 manage.py send_msg
```


## 貢獻此專案

### Server Flows

![](https://i.imgur.com/FzozhTL.png)


### 新增爬蟲

- 新增 學校/系所：
    - 在 `backend/crawler` 資料夾中，編輯 `crawl.py`, `url_list.json`.

### 新增 command:

- 在 `backend/management/commands` 資料夾，自行新增檔案.

### 編輯聊天機器人設定

- 在 `backend/MSG` 中有 `line.py` 與 `tg.py`

### 調整資料庫

- `backend/models.py`

## 部署（自動運行）

將下面兩個指令放到 crontab 中。

```bash
python3 manage.py crawl nthu nctu
python3 manage.py send_msg
```

## TODO

- [ ] LINE Notify 機器人
- [x] Telegram Channel 機器人
- [ ] 註冊 LINE Notify 的網頁


###### tags: `Telegram` `NTHU`
