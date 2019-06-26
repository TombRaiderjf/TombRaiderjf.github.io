#!/usr/bin/python
# -*- coding: UTF-8 -*-

# author Acha 2019/6/17
import sys
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests
import random
import MySQLdb

menpai_dict = {"少林": 0, "明教": 1, "丐帮": 2, "武当": 3, "峨嵋": 4, "星宿": 5 ,"天龙": 6, "天山": 7, "逍遥": 8, "慕容": 9, "唐门":10, "鬼谷": 11}

sex_dict = {"女": 0, "男": 1}

# get the page information of all the goods in sale
def getData(url):
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
        time.sleep(1)
        name = item.find('span', class_='name').get_text()
        name_pure = name[1: len(name)-1]
        price = item.find('p', class_='price').get_text()[1:]
        url_this = item.find('a', class_='r-img').get('href')
        id = url_this.split("=")[1]        
        split_str = name_pure.split(" ")
        menpai = menpai_dict[split_str[0]]
        sex = sex_dict[split_str[1]]
        rank = split_str[2]
        rank_pure = rank[0: len(rank)-1]
        chonglou = False
        if item.find('i', class_='icon-cl'):
            chonglou = True
        html_this = requests.get(url_this, headers=header)
        if html_this.status_code == 200:
            soup_this = BeautifulSoup(html_this.content, "html.parser", from_encoding='utf-8')
            bottom = soup_this.find('div', class_='fn-fix-info')
            btm_info = bottom.find_all('span', class_='span')
            score_equipment = btm_info[1].get_text()

            if int(score_equipment) < 50000:
                return True

            score_diamond = btm_info[6].get_text()
            right = soup_this.find('div', class_='h422')
            blood = right.find('i', class_='fn-high-light').get_text()
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
            print(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level) 
            write_data(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level)
        else:
            print("error")
    return false


def write_data(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level):
    sql = "insert into goods value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(id, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level)
    try:       
        cursor.execute(sql)       
        db.commit()
    except:
        db.rollback()


# load the user-agent file into a list
def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


db = MySQLdb.connect('localhost', 'root', 'hc7783au', 'tl')
cursor = db.cursor()
agentHeaders = LoadUserAgents("user_agents.txt")
t1 = datetime.now()
raw_url = "http://tl.cyg.changyou.com/goods/selling&order_by=equip_point-desc?&page_num="
for i in range(1, 20):
    flag = getData(raw_url+str(i))
    if flag:
        break
t2 = datetime.now()
print("time=", (t2-t1).seconds)
cursor.close()
db.close()

# create table goods (id varchar(20) primary key,
# sex int not null,
# chonglou int not null,
# price int not null,
# menpai int not null,
# rank int not null,
# score_equipment int not null,
# score_diamond int not null,
# blood int not null,
# max_attack int not null,
# max_attribute int not null,
# wuyi_level int not null);