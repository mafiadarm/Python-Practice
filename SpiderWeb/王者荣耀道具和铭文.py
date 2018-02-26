# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_14_2018  21:29
   File Name:      /GitHub/崩崩崩
   Creat From:     PyCharm
   Python version: 3.6.4
- - - - - - - - - - - - - - -
   Description:
   铭文和道具，放到excel里面
==============================
"""
import json
import os
import requests
from xlwt import Workbook
import logging


__author__ = 'Loffew'


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

'''
<li><a href=(\"herodetail/(*.?)\.shtml\")*.? alt=(*.?)*.?</li>
group1 = 拼接地址
group2 = 编号
group3 = 名字
DOC_AFTER = http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/179/179-bigskin-2.jpg
DOC_ADDRESS = AFTER + group1  # 此地址用来找技能说明的文本
PIC = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/178/178-bigskin-3.jpg"
PIC_ADDRESS = PIC + 编号 + "/" + 编号 + "-bigskin-" + i + ".jpg"
'''

head = {  # 直接在请求里面复制，如果要带就在get里面增加headers=head
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.2;Trident/6.0)'
}

folder = "王者荣耀皮肤"
if not os.path.exists(folder):
    os.mkdir(folder)

# 获取全铭文
ming_url = "http://pvp.qq.com/web201605/js/ming.json"
resp = requests.get(ming_url)  # 拿到的是json
tt = resp.content.decode()  # 转json格式
ss = json.loads(tt)  # 接上面转json格式

workbook = Workbook(encoding="utf-8")
file_name = "铭文"
sheet_y = workbook.add_sheet("yellow")
sheet_b = workbook.add_sheet("blue")
sheet_r = workbook.add_sheet("red")
y, b, r = 0, 0, 0
for i in ss:
    ming_id = i.get('ming_id')  # 编号
    ming_type = i.get('ming_type')  # 颜色
    ming_grade = i.get('ming_grade')  # 级别
    ming_name = i.get('ming_name')  # 名字
    ming_des = i.get('ming_des')  # 数值

    ll = [ming_id, ming_name, ming_grade, ming_type, ming_des]

    if ming_type == "yellow":
        for index, value in enumerate(ll):
            sheet_y.write(y, index, value)
        y += 1
    elif ming_type == "blue":
        for index, value in enumerate(ll):
            sheet_b.write(b, index, value)
        b += 1
    elif ming_type == "red":
        for index, value in enumerate(ll):
            sheet_r.write(r, index, value)
        r += 1

workbook.save("{}/{}.xls".format(folder, file_name))

# 道具一览表
item_url = "http://pvp.qq.com/web201605/js/item.json"
resp = requests.get(item_url)  # 拿到的是json
tt = resp.content.decode()  # 转json格式
ss = json.loads(tt)  # 接上面转json格式

workbook = Workbook(encoding="utf-8")
file_name = "道具"
sheet_i = workbook.add_sheet("items")

for index, i in ss:
    item_id = i.get("item_id")  # 编号
    item_name = i.get("item_name")  # 名称
    item_type = i.get("item_type")  # 级别
    price = i.get("price")  # 卖
    total_price = i.get("total_price")  # 买
    des1 = i.get("des1")  # 属性
    des2 = i.get("des2")  # 唯一属性

    ll = [item_id, item_name, item_type, price, total_price, des1, des2]

    for j, k in enumerate(ll):
        sheet_i.write(index, j, k)

workbook.save("{}/{}.xls".format(folder, file_name))
