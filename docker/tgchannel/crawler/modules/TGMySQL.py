# coding=utf-8

import pymysql
import time


class TGMySQL:
    def __init__(self, user="william", password="william", db_name="TESTDB"):
        flag = True
        while flag:
            try:
                self.db = pymysql.connect("db", "william", "william", "TESTDB")
                flag = False
            except:
                print("等待 SQL Server 啟動")
                time.sleep(1)

        self.cursor = self.db.cursor()
        print("Connected db")

    def connect_SQL(self, tableName):
        sql = """CREATE TABLE %s(
            TITLE  CHAR(80) NOT NULL,
            LINK  CHAR(200),
            DATA CHAR(20))
            """ % tableName
        try:
            self.cursor.execute(sql)
        except:
            print("找到資料表：%s" % tableName)

    def check_SQL(self, tableName, title):
        sql = "SELECT count( * ) FROM `%s` WHERE `TITLE` = '%s'" % (tableName, title)
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
