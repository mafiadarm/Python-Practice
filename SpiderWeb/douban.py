#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           03_24_2018  20:39
  File Name:      /GitHub/douban
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  通过XHR的头信息追踪json内容来获取文字内容
==============================
"""
import logging
import random
import json
import jsonpath
import requests
import time

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


class DouBanSpider(object):
    def __init__(self):
        self.start = 0
        self.user_agents = [
        'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
        'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)',
        'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv',
        'Mozilla/5.0(WindowsNT6.1;rv',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
        ]
        self.json_data = None
        self.item = {}

    def startWork(self):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(self.start) + "&limit=20"

        response = requests.get(url, headers={"user-agent": random.choice(self.user_agents)})
        print(url)
        if response.text == "[]":
            return
        pp_dbg(response.status_code)
        self.jsonData(response.text)

    def jsonData(self, data):
        data = json.loads(data)
        pp_dbg(type(data))

        # 电影名称
        title_list = jsonpath.jsonpath(data, "$..title")
        # 影片评分
        score_list = jsonpath.jsonpath(data, "$..score")
        # 电影地址
        url_list = jsonpath.jsonpath(data, "$..url")
        # 电影类型
        types_list = jsonpath.jsonpath(data, "$..types")
        # 制片地区
        regions_list = jsonpath.jsonpath(data, "$..regions")

        for title, score, url, types, regions in zip(title_list, score_list, url_list, types_list, regions_list):
            self.item["title"] = title
            self.item["score"] = score
            self.item["url"] = url
            self.item["types"] = types
            self.item["regions"] = regions
            pp_dbg(self.item)
            self.writeData()

        self.start += 20
        time.sleep(random.randint(1, 2))
        self.startWork()

    def writeData(self):
        content = json.dumps(self.item, ensure_ascii=False) + ",\n"  # 关闭默认转码为2进制
        with open("Douban.json", "a", encoding="utf-8") as rr:
            rr.write(content)

if __name__ == '__main__':
    work = DouBanSpider()
    work.startWork()