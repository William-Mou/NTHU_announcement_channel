#coding=utf-8
import os
import sys
import telepot
import requests
from bs4 import BeautifulSoup
import  pymysql
import time

sys.setrecursionlimit(40000)

r = requests.get('http://ipth.web.nthu.edu.tw/bin/home.php?Lang=zh-tw')
r.encoding='utf-8'
content = r.text

soup = BeautifulSoup(content, 'lxml') 

TOKEN = "871956208:AAHisfa3fJKMl6l6ODvD8dbwpiw97gIfuw8"
bot = telepot.Bot(TOKEN)
#time.sleep(100)
db = pymysql.connect("db","william","william","TESTDB" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
    TITLE  CHAR(80) NOT NULL,
    LINK  CHAR(200),
    DATA CHAR(20),
                """
cursor.execute(sql)
db.close()


news_data = {}
tables = soup.find_all(class_ = 'mc')
for announce in tables:
    # 新增新的資料
    #print(announce)
    
    news = announce.find(class_ = 'ptname').a
    data = announce.find(class_ = 'date')
    if news.string in news_data:
        print("沒有新的文章了")
    else:
        news_data[news.string] = {"title": news.string,
                          "link" : news.get('href'),
                          "data" : str(data.string).split()[1] }
        bot.sendMessage(-1001429244108, news_data[news.string]["title"] + "\n" + news_data[news.string]["link"])
    
        print("新增一筆新的文章")


