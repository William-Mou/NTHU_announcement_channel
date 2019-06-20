#coding=utf-8
import os
import sys
import telepot
import requests
from bs4 import BeautifulSoup
import  pymysql
import time

class SQL:
    def __init__:
        flag = True
        while flag:
            try:
                db = pymysql.connect("db","william","william","TESTDB" )
                flag = False
            except:
                print("等待 SQL Server 啟動")
                time.sleep(1)

    def connect_SQL(tableName):
        # 新增 DB 欄位
        cursor = db.cursor()
        sql = """CREATE TABLE %s(
            TITLE  CHAR(80) NOT NULL,
            LINK  CHAR(200),
            DATA CHAR(20))
            """%tableName
        try:
            cursor.execute(sql)
        except:
            print("找到資料表：%s" %tableName )
        db.close()

    def check_SQL():
        sql = "SELECT count( * ) FROM `NTHU_IPTH` WHERE `TITLE` = '%s'" % (str(news.string))
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        db.close()
        if result == 0:
            return True
        else:
            return False

    def insert_SQL(TITLE, LINK, DATA):
        sql = "INSERT INTO NTHU_IPTH(TITLE, LINK, DATA) VALUES ('%s', '%s', '%s')" % (TITLE, LINK, DATA)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()


def crawler():
    # 爬蟲
    r = requests.get('http://ipth.web.nthu.edu.tw/bin/home.php?Lang=zh-tw')
    r.encoding='utf-8'
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    tables = soup.find_all(class_ = 'mc')
    return tables

def main():
# 遍歷並通知
    bot = telepot.Bot(os.environ["TELEPOT_TOKEN"])
    tables = crawler()
    for announce in tables:
        news = announce.find(class_ = 'ptname').a
        data = announce.find(class_ = 'date')
        
        nonexistent = check_SQL()
        
        if nonexistent :
            insert_SQL( str(news.string), str(news.get('href')), str(str(data.string).split()[1]) )
            try:
                bot.sendMessage(-1001429244108, news.string + "\n" + news.get('href') )
                print("新增一筆新的文章：", news.string)
            except:
                print("time out :", news.string )
        else:
            print("沒有新的文章了")


