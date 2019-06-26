#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定时更新Mysql数据表

import sys
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests
import random
from crawl import LoadUserAgents
import MySQLdb


def updateUrl(url):
    header = {
     'User-Agent': random.choice(agentHeaders)
    }
    while(True):
        html = requests.get(url, headers=header)
        if html.status_code == 200:
            break
        time.sleep(1)
    soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
    goods = soup.find_all('li', class_='role-item')
    for item in goods:
        url_this = item.find('a', class_='r-img').get('href')
        id = url_this.split("=")[1] 
        price = item.find('p', class_='price').get_text()[1:]
        updateData(id, price)


def getData(url):


def updateData(id, price):
    sql = "select * from goods where id=" + id
    try:       
        cursor.execute(sql)  
        data = cursor.fetchone() 
        if data != None:
            if data
            insert = "insert into goods value()"
            print("insert new value " + str(id))
        db.commit()
    except:
        db.rollback()


db = MySQLdb.connect('localhost', 'root', 'hc7783au', 'tl')
cursor = db.cursor()
agentHeaders = LoadUserAgents("user_agents.txt")
t1 = datetime.now()
raw_url = "http://tl.cyg.changyou.com/goods/selling&order_by=equip_point-desc?&page_num="
for i in range(1, 100):
    updateUrl(raw_url+str(i))
t2 = datetime.now()
print("time=", (t2-t1).seconds)
cursor.close()
db.close()