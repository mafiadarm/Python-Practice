# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_29_2018  15:18
   File Name:      /GitHub/wechat_friends_information
   Creat From:     PyCharm
   Python version:   
- - - - - - - - - - - - - - - 
   Description:    抓取微信朋友信息
==============================
"""

__author__ = 'Loffew'

import logging
import itchat
import time
from xlwt import Workbook
from collections import Counter

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


# itchat.auto_login(hotReload=True)
itchat.login()
friends = itchat.get_friends(update=True)[0:]
fire_name = Workbook(encoding="utf-8")
file_name = time.time()

male, female, other = 0, 0, 0
provinces = []
cities = []
informational = [("网名", "备注名", "省", "市", "性别", "保存信息条数", "签名")]

for friend in friends:
    sex = friend["Sex"]
    if sex == 1:
        friend["Sex"] = "男"
        male += 1
    elif sex == 2:
        friend["Sex"] = "女"
        female += 1
    else:
        friend["Sex"] = "保密"
        other += 1
    informational.append((friend['NickName'], friend['RemarkName'], friend['Province'], friend['City'], friend['Sex'],
                          friend['SnsFlag'], friend['Signature']))

    cities.append(friend["Province"] + "_" + friend["City"])
    provinces.append(friend["Province"])

cities_con = Counter(cities)
province_con = Counter(provinces)
total = sum([male, female, other])

sheet_i = fire_name.add_sheet("information")
for row, inf in enumerate(informational):
    for col, v in enumerate(inf):
        sheet_i.write(row, col, v)

sheet_p = fire_name.add_sheet("provinces")
for k, v in enumerate(province_con.items()):
    sheet_p.write(k, 0, str(v[0]))
    sheet_p.write(k, 1, v[1])

sheet_c = fire_name.add_sheet("cities")
for k, v in enumerate(cities_con.items()):
    sheet_c.write(k, 0, str(v[0]))
    sheet_c.write(k, 1, v[1])

sheet_s = fire_name.add_sheet("sex")
sheet_s.write(0, 0, "男性好友")
sheet_s.write(0, 1, float(male) / total)
sheet_s.write(1, 0, "女性好友")
sheet_s.write(1, 1, float(female) / total)
sheet_s.write(2, 0, "不明性别好友")
sheet_s.write(2, 1, float(other) / total)

with open("%s.txt" % file_name, "w", encoding="utf-8") as ff:
    ff.writelines(str(friends))

fire_name.save("%s.xls" % file_name)
itchat.logout()
