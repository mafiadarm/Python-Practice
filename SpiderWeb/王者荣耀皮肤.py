# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_14_2018  21:29
   File Name:      /GitHub/崩崩崩
   Creat From:     PyCharm
   Python version: 3.6.4
- - - - - - - - - - - - - - -
   Description:
   下载王者荣耀高清皮肤图
==============================
"""
import json
import random
import os
import requests
import time
from xlwt import Workbook
import logging


__author__ = 'Loffew'


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

'''
以女娲为标准
访问网址为：http://pvp.qq.com/web201605/herolist.shtml
    头像图片为： http://game.gtimg.cn/images/yxzj/img201606/heroimg/179/179.jpg
    尾巴拼接部分：herodetail/179.shtml
    实际链接地址：http://pvp.qq.com/web201605/herodetail/179.shtml
    两个拼接为 "http://pvp.qq.com/web201605/herodetail/{}.shtml"
        # 得到拼接部分：http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/179/179-bigskin-2.jpg
大图地址：http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/178/178-bigskin-3.jpg
测试得知bigskin后面的数字为连续的，直到出现404

.shtml的都不是真是地址，以抓包为准

所以我们需要得到的是编码 178类的数字，另外要以名字来命名文件夹
从1开始遍历到链接返回404为止
'''

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

# 获取全图片
list_url = "http://pvp.qq.com/web201605/js/herolist.json"
resp = requests.get(list_url)  # 拿到的是json
tt = resp.content.decode()  # 转json格式
ss = json.loads(tt)  # 接上面转json格式

folder = "王者荣耀皮肤"
if not os.path.exists(folder):
    os.mkdir(folder)

for i in ss:
    ename = i.get("ename")  # 编号
    cname = i.get("cname")  # 名字
    folder_name = "{}/{}/".format(folder, cname)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    skin_name = i.get("skin_name")  # 皮肤
    skin_name = skin_name.split("|")
    skin_range = len(skin_name)

    PIC = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg"
    for num in range(skin_range):
        time.sleep(random.random())
        PIC_ADDRESS = PIC.format(ename, ename, num+1)
        image = requests.get(PIC_ADDRESS)
        pic_name = folder_name + skin_name[num] + ".jpg"
        with open(pic_name, "wb") as pp:
            pp.write(image.content)
