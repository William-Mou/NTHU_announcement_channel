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

TOKEN = ""
bot = telepot.Bot(TOKEN)
time.sleep(100)
db = pymysql.connect("db","william","william","TESTDB" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS NTHU_IPTH")
sql = """CREATE TABLE NTHU_IPTH (
    TITLE  CHAR(80) NOT NULL,
    LINK  CHAR(200),
    DATA CHAR(20))
    """
cursor.execute(sql)
#cursor.close()


news_data = {}
tables = soup.find_all(class_ = 'mc')
for announce in tables:
    # 新增新的資料
    #print(announce)
    
    news = announce.find(class_ = 'ptname').a
    data = announce.find(class_ = 'date')
    
    sql = "SELECT count( * ) FROM `NTHU_IPTH` WHERE `TITLE` = '%s'" % (str(news.string))
    cursor.execute(sql)
    result = cursor.fetchone()
    print(sql)
    print(result)
    if result[0] == 0:
        sql = "INSERT INTO NTHU_IPTH(TITLE, LINK, DATA) VALUES ('%s', '%s', '%s')" %\
        (str(news.string), str(news.get('href')), str(str(data.string).split()[1]) )
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
                #news_data[news.string] = {"title": news.string,
                #         "link" : news.get('href'),
#         "data" : str(data.string).split()[1] }
        bot.sendMessage(-1001429244108, news.string + "\n" + news.get('href') )
    
        print("新增一筆新的文章")
    else:
        print("沒有新的文章了")



db.close()
