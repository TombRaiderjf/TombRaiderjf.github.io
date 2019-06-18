# author Acha 2019/6/17
import sys
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests
import random
import MySQLdb


# get the page information of all the goods in sale
def getData(url, userAgent):
    header = {
     'User-Agent': userAgent
    }
    while(True):
        html = requests.get(url, headers=header)
        if html.status_code == 200:
            break
        sleep(1)
    soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
    goods = soup.find_all('li', class_='role-item')
    for item in goods:
        name = item.find('span', class_='name')
        score_equipment = item.find('b')
        price = item.find('p', class_='price')
        id = item.find('a', class_='r-img').get('href').split("=")[1]
        chonglou = False
        if item.find('i', class_='icon-cl'):
            chonglou = True
        print(name.get_text(), score_equipment.get_text(), price.get_text(), id, chonglou)


# load the user-agent file into a list
def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


if __name__ == '__main__':
    agentHeaders = LoadUserAgents("user_agents.txt")
    t1 = datetime.now()
    raw_url = "http://tl.cyg.changyou.com/goods/selling?&page_num="
    for i in range(1, 100):
        getData(raw_url+str(i), random.choice(agentHeaders))
    t2 = datetime.now()
    print("time=", (t2-t1).seconds)