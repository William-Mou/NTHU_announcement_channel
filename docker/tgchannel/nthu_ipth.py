#coding=utf-8
import os
import sys
import telepot
import requests
from bs4 import BeautifulSoup
import  pymysql
import time

# 爬蟲
r = requests.get('http://ipth.web.nthu.edu.tw/bin/home.php?Lang=zh-tw')
r.encoding='utf-8'
content = r.text
soup = BeautifulSoup(content, 'lxml') 
tables = soup.find_all(class_ = 'mc')

# telepot
bot = telepot.Bot(os.environ["TELEPOT_TOKEN"])

# 新增 DB 欄位
db = pymysql.connect("db","william","william","TESTDB" )
cursor = db.cursor()
sql = """CREATE TABLE NTHU_IPTH (
    TITLE  CHAR(80) NOT NULL,
    LINK  CHAR(200),
    DATA CHAR(20))
    """
try:
    cursor.execute(sql)
except:
    print("找到資料表：NTHU_IPTH" )

# 遍歷並通知
for announce in tables:
    news = announce.find(class_ = 'ptname').a
    data = announce.find(class_ = 'date')
    
    sql = "SELECT count( * ) FROM `NTHU_IPTH` WHERE `TITLE` = '%s'" % (str(news.string))
    cursor.execute(sql)
    result = cursor.fetchone()
    
    if result[0] == 0:
        sql = "INSERT INTO NTHU_IPTH(TITLE, LINK, DATA) VALUES ('%s', '%s', '%s')" %\
        (str(news.string), str(news.get('href')), str(str(data.string).split()[1]) )
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        try:
            bot.sendMessage(-1001429244108, news.string + "\n" + news.get('href') )
            print("新增一筆新的文章：", news.string)
        except:
            print("time out :", news.string )
    else:
        print("沒有新的文章了")
db.close()

