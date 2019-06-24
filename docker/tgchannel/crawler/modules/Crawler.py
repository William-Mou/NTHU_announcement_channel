import requests
from bs4 import BeautifulSoup

def Crawler(ta_link="http://ipth.web.nthu.edu.tw/bin/home.php?Lang=zh-tw", find_all_class="mc"):
    r = requests.get(ta_link)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    tables = soup.find_all(class_=find_all_class)
    return tables