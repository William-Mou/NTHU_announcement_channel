
from modules import TGMySQL
import telepot
import os
import json
import requests
from bs4 import BeautifulSoup
import re

def send_msg(office, title, link):
    bot = telepot.Bot(os.environ["TELEPOT_TOKEN"])

    try:
        bot.sendMessage(-1001429244108,  office + "公告：\n" + title +  "\n" + link)
        print("新增一筆新的文章：", title)
    except:
        print("time out :", title)

def crawler(office, ta_link, SQL):
    r = requests.get(ta_link)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    tables = soup.find_all(class_="announcement-item")
    #print(tables)

    for announce in tables:
        try:
            #print(announce)
            title = str(announce.find_all("a")[0].string).strip()
            title = str(title).strip()
            link = announce.find_all("a")[0]['href']
            data = announce.find_all("span")
            data = str(data).split("\n")[-2].split()[0]
            
            print(title)
            print(link)
            print(data)
            if type(data) == None:
                data = None
            else:
                data = data
        except:
            pass

        nonexistent = SQL.check_SQL(title)
        if nonexistent:
            SQL.insert_SQL(title, office, link, data)
            send_msg(office, title, link)
        else:
            print("沒有新的文章了")

def main():
    file_name = os.path.basename(__file__)
    SQL = TGMySQL.TGMySQL(file_name)
    SQL.connect_SQL()

    with open('/usr/src/app/crawler/resource/nctu_cs.json' , 'r') as reader:
        jf = json.loads(reader.read())

    for key in jf:
        crawler(office=key, ta_link=jf[key], SQL=SQL)

    SQL.close_SQL()


if __name__ == "__main__":
    main()
