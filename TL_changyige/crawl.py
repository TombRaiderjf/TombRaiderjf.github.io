import sys
from bs4 import BeautifulSoup
import time
import requests

def getData(url):
    header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
    goods = soup.find_all('li', class_='role-item')
    for item in goods:
        name = item.find('span', class_='name')
        score_equipment = item.find('b')
        print(name.get_text(), score_equipment.get_text())




if __name__ == '__main__':
    raw_url = "http://tl.cyg.changyou.com/goods/selling?&page_num=1"
    getData(raw_url)