import requests
from bs4 import BeautifulSoup
from .url_list import NTHU_CS
from backend.MSG import tg
from backend.models import News

def crawler(office, ta_link):
    r = requests.get(ta_link)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    tables = soup.find_all(class_="mc")

    for announce in tables:
        try:
            title = announce.find(class_ = 'ptname').a.string
            title = str(title).strip()
            url = announce.find(class_ = 'ptname').a.get('href')
            data = announce.find(class_ = 'date')
            if type(data) == None:
                data = None
            else:
                data = data.string.split()[1] 
        except:
            pass
            print(title)
            News.objects.add(dep='CS', category=office, title=title, url=url)

        
def do():
    for key in NTHU_CS:
        crawler(office=key, ta_link=NTHU_CS[key])

