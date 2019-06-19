#coding=utf-8

import dill
import os
import sys
import telepot
import requests
from bs4 import BeautifulSoup

sys.setrecursionlimit(40000)

r = requests.get('http://ipth.web.nthu.edu.tw/bin/home.php?Lang=zh-tw')
r.encoding='utf-8'
content = r.text

soup = BeautifulSoup(content, 'lxml') 

TOKEN = "871956208:AAHisfa3fJKMl6l6ODvD8dbwpiw97gIfuw8"
bot = telepot.Bot(TOKEN)

def init():
    if (not os.path.isfile("./news_file")) or os.path.getsize("./news_file") == 0:
        print("init")
        with open("./news_file", 'wb') as news_file:
            dill.dump({}, news_file)

init()


f= open('./news_file', 'rb')
onews_data = dill.load(f)
f.close()


tables = soup.find_all(class_ = 'mc')
for announce in tables:
    # 新增新的資料
    try:
        news = announce.find(class_ = 'ptname').a
        data = announce.find(class_ = 'date')
        if news.string in news_data:
            print("沒有新的文章了")
        else:
            news_data[news.string] = {"title": news.string, 
                              "link" : news.get('href'),
                              "data" : str(data.string).split()[1] }
            print(news_data[news.string])
            #bot.sendMessage(-1001429244108, news_data[news.string]["title"] + "\n" + news_data[news.string]["link"])
            print("新增一筆新的文章")
#    except AttributeError:
#   pass
    except :
        pass 

os.remove('./news_file')
# 儲存資料到硬碟
f = open('./news_file', 'wb')
dill.dump(news_data, f)
f.close()
