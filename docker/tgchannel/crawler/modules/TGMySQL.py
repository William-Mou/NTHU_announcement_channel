# coding=utf-8

import pymysql
import time
import os
class TGMySQL:
    def __init__(self, user="william", password="william", db_name="TESTDB"):
        flag = True
        while flag:
            try:
                self.db = pymysql.connect("db","william","william","TESTDB" )
                flag = False
            except:
                print("等待 SQL Server 啟動")
                time.sleep(1)

        self.cursor = self.db.cursor()
        print("Connected db")

    def connect_SQL(self, tableName):
        # 新增 DB 欄位
        sql = """CREATE TABLE %s(
            TITLE  CHAR(80) NOT NULL,
            LINK  CHAR(200),
            DATA CHAR(20))
            """ % tableName
        try:
            self.cursor.execute(sql)
        except:
            print("找到資料表：%s" % tableName)

    def check_SQL(self, title):
        sql = "SELECT count( * ) FROM `NTHU_IPTH` WHERE `TITLE` = '%s'" % title
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        if result == 0:
            return True
        else:
            return False

    def insert_SQL(self, TITLE, LINK, DATA):
        sql = "INSERT INTO NTHU_IPTH(TITLE, LINK, DATA) VALUES ('%s', '%s', '%s')" % (
            TITLE, LINK, DATA)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def close_SQL(self):
        self.db.close()

# def main():
#     # 遍歷並通知
#     bot = telepot.Bot(os.environ["TELEPOT_TOKEN"])
#     tables = crawler()
#     for announce in tables:
#         news = announce.find(class_='ptname').a
#         data = announce.find(class_='date')

#         nonexistent = check_SQL()

#         if nonexistent:
#             insert_SQL(str(news.string), str(news.get('href')),
#                        str(str(data.string).split()[1]))
#             try:
#                 bot.sendMessage(-1001429244108, news.string +
#                                 "\n" + news.get('href'))
#                 print("新增一筆新的文章：", news.string)
#             except:
#                 print("time out :", news.string)
#         else:
#             print("沒有新的文章了")
