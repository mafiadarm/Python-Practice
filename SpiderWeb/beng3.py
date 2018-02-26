# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_30_2018  12:00
   File Name:      /GitHub/崩崩崩
   Creat From:     PyCharm
   Python version: 下载蹦蹦蹦的角色图
- - - - - - - - - - - - - - - 
   Description:
==============================
"""
import re

import os
import requests
import logging

__author__ = 'Loffew'


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'  # 没用到
head = {
    "User-Agent": User_Agent
}
url = "https://www.bh3.com/valkyria.html"  # 这个网页找到图片所有信息[每个网页的相同处]

response = requests.get(url)  # 发现有所有角色名称
print(response.status_code)  # 打印状态码

rxg = re.compile(r"card-(.*?)\"")  # 建正则匹配这些名字
foots = set(rxg.findall(response.text))  # 发现有多余的匹配项
foots.remove("name")  # 删除多余的匹配项

image_url = "https://static.event.mihoyo.com/bh3_homepage/images/valkyria/album/%s.png"  # 审查元素发现原图地址
folder = "beng3/"
if not os.path.exists(folder):
    os.mkdir(folder)

for foot in foots:
    image_path = image_url % foot.replace("-", "_")  # 拼接地址
    with open(folder + "%s.png" % foot, "wb") as ff:  # 下载图片[图片等多媒体需要加“b”]
        image = requests.get(image_path)
        ff.write(image.content)  # 保存图片用content