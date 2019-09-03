# -*- coding: utf-8 -*- 
import sys
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests
import random
import MySQLdb
import json
import re
from flask import Flask, request, jsonify
from flask_cors import CORS

clothes_dict = {10124637: "a", 10125199: "b", 10125028: "c", 10124724: "c", 10124607: "d", 10125133: "d", 10125055: "e", 10124405: "f", 10124404: "g",
10124403: "h", 10124542: "i", 10125108: "j"}

ride_dict = {"沧澜羽翼": "a", "金羽": "b", "梦灵仙驹": "c", "青翼战龙": "d", "添福锦鳞": "e", "水碧飞鸢": "f", "绒雪神牛": "g", "黑天马": "h", "紫电": "i", \
    "月白龙马": "j", "四喜送鲤台": "k", "绝云焱龙": "l", "熔岩魔犀": "m", "绛紫飞鸢": "n", "梦幻仙驹": "o", "霸世羽龙": "p"}


menpai_dict = {"少林": 0, "明教": 1, "丐帮": 2, "武当": 3, "峨嵋": 4, "星宿": 5 ,"天龙": 6, "天山": 7, "逍遥": 8, "慕容": 10, "唐门":11, "鬼谷": 12}

sex_dict = {"女": 0, "男": 1}

server_dict = {
    14:  "易筋经",
    22:  "水晶湖", 
    38:  "九阴真经", 
    47:  "神龙摆尾",
    65:  "黄果树",
    68:  "一阳指",
    85:  "妖界", 
    101: "紫禁之巅",
    111: "八达岭", 
    118:  "北戴河", 
    134:  "凤凰山",
    137: "太湖仙岛",
    149: "雨花台", 
    154: "双龙洞",
    155: "上海滩", 
    162:  "张家界", 
    168: "武夷山",
    172:  "冥界", 
    182:  "洞庭秋月",
    188: "阿朱", 
    191:  "蜀南竹海",
    198: "剑门蜀道", 
    209:  "昆仑山", 
    1010: "烧刀子", 
    1015: "云雾茶", 
    1042: "三生石", 
    1043: "问情崖", 
    1053: "什刹海", 
    1138: "百泉书院", 
    1161: "千寻塔", 
    1171: "乐山大佛",
    1191: "五峰书院", 
    2020: "峨嵋山", 
    2021:  "天蝎座", 
    2082:  "不冻泉", 
    2093:  "锦绣中华", 
    2201: "听香水榭",
    2202:  "极冰凝杀", 
    3016: "仙侣情缘",
    3048:  "天若有情", 
    3079: "九天惊雷", 
    3081:  "唯我独尊", 
    3085:  "万敌不侵", 
    3125:  "天下第一", 
    3128:  "烽火连城",
    3144: "金风玉露", 
    3145:  "天一阁", 
    3161:  "刀光剑影",
    3192:  "独孤求败",
    3200:  "天龙",
    3202:  "天下",
    4025:  "紫电青霜", 
    4036:  "武林至尊",
    5013: "天命",
    5016:  "幻影", 
    5024: "宠爱一生", 
    5038:  "一世长安", 
    5057:  "千秋殿", 
    5060:  "英雄战歌", 
    5065:  "一代宗师", 
    5068: "三世情缘", 
    5069: "天下为棋", 
    5072:  "只手遮天", 
    5074:  "十里桃花",
    5075:  "醉梦江南",
    5076: "不见不散", 
    5083: "一梦十年",
    5084: "金戌迎瑞",
    5087: "天下会武",
    5088: "守望江湖",
    5089: "在水一方",
    5090: "铜锣湾",
    5091: "宁为我道",
    5092: "师门逆徒",
    5093: "逐梦江湖",
    5094: "鸿运连年",
    5095: "鸿运当头",
    5096: "瑞鹤千秋",
    5097: "鹤舞九霄",
    5098: "愿君共白首",
    5099: "以梦为马",
    5120: "惜君青玉裳",
    9066: "争霸赛一区",
    9140: "烟雨轩",
}


baseUrl = "http://tl.cyg.changyou.com/goods/char_detail?serial_num="
id_str="20190817843370502"



def addData(id, method, info):
    url = baseUrl + id
    header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    html = requests.get(url, headers=header)
    if html.status_code == 200:
        try:
            soup = BeautifulSoup(html.content, "html.parser")
            price = soup.find('span', class_='ui-money-color').get_text()[1:]
            server_str = soup.find('p', class_='server-info').get_text()
            for key in server_dict:
                if server_str.find(server_dict[key]) != -1:
                    server = key
            index_data = html.text.find('charObj')
            to_data = html.text.find(';', index_data)
            data = html.text[index_data+10: to_data]
            dict_data = json.loads(data)  # str转为dict
            sex = str(dict_data['sex'])
            menpai = str(dict_data['menpai'])
            rank = str(dict_data['level'])
            score_equipment = str(dict_data['equipScore'])
            chonglou = "0"
            if dict_data['CLNum'] != 0:
                chonglou = "1"
            wuyi_level = str(dict_data['martialDB']['martialLevel'])
            shending1 = dict_data['shenDing']['danYaoCount']
            shending2 = dict_data['shenDing']['lianDanCount']
            shending_index1 = 0
            shending_index2 = 0
            for m in range(1, 10):
                if (shending1 - m) >=0:
                    shending_index1 = m
                    shending1 -= m
                if (shending2 - m) >=0:
                    shending_index2 = m
                    shending2 -= m
            shending = shending_index2 + 10*shending_index1
            score_diamond = str(dict_data['gemJinJieScore'])
            blood = str(dict_data['maxHp'])
            attack_arr = [dict_data["coldAtt"], dict_data["fireAtt"], dict_data["lightAtt"], dict_data["postionAtt"] ]     
            max_attack = max(attack_arr)
            max_attribute = str(attack_arr.index(max_attack))
            ride = ""
            clothes = ""
            for item in dict_data['items']['equip']:
                if dict_data['items']['equip'][item]['typeDesc'] == "时装":
                    for key in clothes_dict:
                        if clothes.find(clothes_dict[key])==-1 and key == dict_data['items']['equip'][item]['dataId']:
                            clothes += clothes_dict[key]
                if dict_data['items']['equip'][item]['typeDesc'] == "坐骑":
                    for key in ride_dict:
                        if ride.find(ride_dict[key])==-1 and dict_data['items']['equip'][item]['name'].find(key) != -1:
                            ride += ride_dict[key]
            if ride == "":
                ride = "0"
            if clothes == "":
                clothes = "0"
            print(id, method, server, sex, chonglou, price, menpai, rank, score_equipment, score_diamond, blood, max_attack, max_attribute, shending, wuyi_level, clothes, ride, info)
            flag = write_data(id, method, server, sex, chonglou, price, menpai, rank, score_equipment, score_diamond, blood, max_attack, max_attribute, shending, wuyi_level, clothes, ride, info)
            return flag
        except:
            print("Error: invalid id!")
            return False

def write_data(id, method, server, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, shending, wuyi_level, clothes, ride, contanct):
    # sql = "insert into information value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(id, server, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, wuyi_level, clothes, ride, contanct)
    try:       
        cursor.execute("insert into information value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, method, server, sex, chonglou, price, menpai, rank_pure, score_equipment, score_diamond, blood, max_attack, max_attribute, shending, wuyi_level, clothes, ride,contanct))       
        db.commit()
        print("add new ", id)
        return True
    except:
        db.rollback()
        print("fail to add new ", id)
        return False

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/submitInfo', methods=['POST'])
def post():
    print("-----------------")
    raw_data = request.get_data()
    data = raw_data.decode('utf-8')
    print(data)
    str_data = data.split('&')
    id = str_data[0].split('=')[1]
    method = str_data[1].split('=')[1]
    contact = str_data[2].split('=')[1]
    #print(data)
    res = addData(id, method, contact)
    if res == True:
        return "success"
    else:
        return "error"


db = MySQLdb.connect('localhost', 'root', 'hc7783au', 'tl')
cursor = db.cursor()

if __name__ == "__main__":   
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)
