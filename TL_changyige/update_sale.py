#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 采集公示区数据

import sys
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests
import random
import MySQLdb


clothes_dict = {}

ride_dict = {"沧澜羽翼": "a", "金羽": "b", "梦灵仙驹": "c", "青翼战龙": "d", "添福锦鳞": "e", "水碧飞鸢": "f", "绒雪神牛": "g", "黑天马": "h", "紫电": "i", \
    "月白龙马": "j", "四喜送鲤台": "k", "绝云焱龙": "l", "熔岩魔犀": "m", "绛紫飞鸢": "n", "梦幻仙驹": "o", "霸世羽龙": "p"}


menpai_dict = {"少林": 0, "明教": 1, "丐帮": 2, "武当": 3, "峨嵋": 4, "星宿": 5 ,"天龙": 6, "天山": 7, "逍遥": 8, "慕容": 9, "唐门":10, "鬼谷": 11}

sex_dict = {"女": 0, "男": 1}


def updateId():
    ids = {}
    cl = {}
    for j in range(1, 30):
        updateUrl(raw_url + str(j), ids, cl)
    print("total data ", len(ids))
    return ids, cl


def updateUrl(url, dic, cl):
    header = {
     'User-Agent': random.choice(agentHeaders)
    }
    while(True):
        html = requests.get(url, headers=header)
        if html.status_code == 200:
            break
        time.sleep(1)
    soup = BeautifulSoup(html.content, "html.parser")
    goods = soup.find_all('li', class_='role-item')
    for item in goods:
        url_this = item.find('a', class_='r-img').get('href')
        id = url_this.split("=")[1] 
        price = item.find('p', class_='price').get_text()[1:]
        if int(price) >= 500:
            dic[id] = price
            if item.find('i', class_='icon-cl'):
                cl[id] = 1
            else:
                cl[id] = 0
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
    sql = "delete from sale where id=" + id
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def addData(id, chonglou):
    url = baseUrl + id
    # print(url)
    header = {
     'User-Agent': random.choice(agentHeaders)
    }
    html = requests.get(url, headers=header)
    if html.status_code == 200:
        soup_this = BeautifulSoup(html.content, "html.parser")
        if soup_this.find('div', class_='goods-lock') is None:
            time.sleep(0.5)
            print("already unexist!")
            return
        sex_label = soup_this.find_all('div', class_='row2')[1]
        sex = sex_dict[sex_label.find('span', class_='span').get_text()]
        menpai_label = soup_this.find('span', class_='fn-other-menpai').get_text()
        menpai = menpai_dict[menpai_label.split(':')[1]]
        rank_lable = soup_this.find('span', class_='fn-other-level').get_text()
        string = rank_lable.split(':')
        rank_pure = string[len(string)-1]
        bottom = soup_this.find('div', class_='fn-fix-info')
        btm_info = bottom.find_all('span', class_='span')
        score_equipment = btm_info[1].get_text()
        score_diamond = btm_info[6].get_text()
        right = soup_this.find('div', class_='h422')
        blood = right.find('i', class_='fn-high-light').get_text()
        price = soup_this.find('span', class_='ui-money-color').get_text()[1:]
        wuyi_level = 0
        wuyi_info = soup_this.find('script', id="tab_12").get_text()
        soup_wuyi = BeautifulSoup(wuyi_info, "html.parser", from_encoding='utf-8')
        wuyi_label = soup_wuyi.find('ul', class_="wy_level")
        if wuyi_label:
            wuyi_level = wuyi_label.find('span').get_text()
        attack_label = soup_this.find_all('div', class_='c-o-l')
        max_attack = -1
        max_attribute = -1
        for i in range(4):
            ch = attack_label[i].find('p').get_text().split("+")[1]
            if int(ch) > max_attack:
                max_attack = int(ch)
                max_attribute = i
        # 坐骑
        ride = ""
        for num in range(1, 300):          
            content = soup_this.find("script", id=str(num))
            if content is None:
                continue
            text = content.get_text()
            for key in ride_dict:
                if text.find(key) != -1:
                    ride = ride + ride_dict[key]
        if ride == "":
            ride = "0"
        write_data(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level, ride)
        #time.sleep(0.2)
        

def deleteUnexist(dic):
    sql = "select id from sale"
    number = cursor.execute(sql)
    data = cursor.fetchmany(number)
    total = 0
    for item in data:
        if dic.get(str(item[0])) is None:
            deleteData(str(item[0]))
            total += 1
    print("delete unexist ", total)


def updateData(dic, cl):
    deleteUnexist(dic)
    for key in dic:
        search = "select id price from sale where id=" + key
        try:       
            cursor.execute(search)  
            data = cursor.fetchone() 
            if data is None:
                addData(key, cl[key])               
            elif dic[key] != data['price']:
                change = "update sale set price=" + dic[key] + " where id=" + key
                cursor.execute(change)
                db.commit()
                print("change price ", key)
        except:
            db.rollback()



def write_data(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level, ride):
    # sql = "insert into goods_v2 value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level, 'a', "NULL")
    try:       
        cursor.execute("insert into sale value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level,  "NULL", ride))       
        db.commit()
        print("add new ", id)
    except:
        db.rollback()
        print("fail to add new ", id)


baseUrl = "http://tl.cyg.changyou.com/goods/char_detail?serial_num="
raw_url = "http://tl.cyg.changyou.com/goods/public?&order_by=equip_point-desc&page_num="
db = MySQLdb.connect('localhost', 'root', 'hc7783au', 'tl')
cursor = db.cursor()
agentHeaders = LoadUserAgents("user_agents.txt")
while(True):
    t1 = datetime.now()
    print("------------------------")
    print("start update url")
    newIds, newCl = updateId()
    updateData(newIds, newCl)
    t2 = datetime.now()
    print("one loop time=", (t2-t1).seconds)
cursor.close()
db.close()


newIds, newCl = updateId()
for key in newIds:
    addData(key, newCl[key])


# create table sale (id bigint primary key,
# sex tinyint not null,
# chonglou tinyint not null,
# price int not null,
# menpai tinyint not null,
# rank tinyint not null,
# score_equipment int not null,
# score_diamond int not null,
# blood int not null,
# max_attack int not null,
# max_attribute tinyint not null,
# wuyi_level int not null,
# clothes varchar(10),
# ride varchar(10));