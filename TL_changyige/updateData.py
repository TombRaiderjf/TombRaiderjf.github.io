#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定时更新Mysql数据表

import sys
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests
import random
import MySQLdb

def updateId():
    ids = {}
    for j in range(1, 100):
        id = updateUrl(raw_url + str(j), ids)
    return ids


def updateUrl(url, dic):
    res = []
    header = {
     'User-Agent': random.choice(agentHeaders)
    }
    while(True):
        html = requests.get(url, headers=header)
        if html.status_code == 200:
            print("success: get new page of item!")
            break
        time.sleep(1)
    soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
    goods = soup.find_all('li', class_='role-item')
    for item in goods:
        url_this = item.find('a', class_='r-img').get('href')
        id = url_this.split("=")[1] 
        price = item.find('p', class_='price').get_text()[1:]
        dic[id] = price
    time.sleep(1)


# load the user-agent file into a list
def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


def deleteData(id):
    sql = "delete from goods where id=" + id
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def getItemData(id):
    url = baseUrl + id
    header = {
     'User-Agent': random.choice(agentHeaders)
    }
    html = requests.get(url, headers=header)
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
        

def deleteUnexist(dic):
    sql = "select id from goods"
    number = cursor.execute(sql)
    data = cursor.fetchmany(number)
    for item in data:
        if dic.get(item['id']) is None:
            deleteData(item['id'])


def updateData(dic):
    deleteUnexist(dic)
    # for key in dic:
    #     search = "select id price from goods where id=" + key
    #     try:       
    #         cursor.execute(search)  
    #         data = cursor.fetchone() 
    #         if data is None:
    #             value = getItemData(key)
    #             insert = "insert into goods value " + value
    #         elif dic[key] != data['price']:
    #             change = "update goods set price=" + dic[key] + " where id=" + key
    #             cursor.execute(change)
    #             db.commit()
    #             return
    #     except:
    #         db.rollback()



baseUrl = "http://tl.cyg.changyou.com/goods/char_detail?serial_num="
raw_url = "http://tl.cyg.changyou.com/goods/selling&order_by=equip_point-desc?&page_num="
db = MySQLdb.connect('localhost', 'root', 'hc7783au', 'tl')
cursor = db.cursor()
agentHeaders = LoadUserAgents("user_agents.txt")
# while(){
t1 = datetime.now()
newIds = updateId()
print(newIds)
updateData(newIds)
t2 = datetime.now()
print("one loop time=", (t2-t1).seconds)
# }
cursor.close()
db.close()