from modules import TGMySQL
import telepot
import os
import json
import requests
from bs4 import BeautifulSoup

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
    tables = soup.find_all(class_= "i-annc__title")
    datas = soup.find_all(class_ = "i-annc__postdate-content")
    for i in range(len(tables)):
        announce = tables[i]
        data = datas[i]
        try:
            title = str(announce.string).strip()
            print("NCTU_EE:",title)
            link = "https://www.dece.nctu.edu.tw/"
            link += str(announce.get("href"))
            data = str(data).split()[-1][:-7]
            
            if type(data) == None:
                data = None
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

    with open('/usr/src/app/crawler/resource/nctu_ee.json' , 'r') as reader:
        jf = json.loads(reader.read())

    for key in jf:
        crawler(office=key, ta_link=jf[key], SQL=SQL)

    SQL.close_SQL()


if __name__ == "__main__":
    main()
