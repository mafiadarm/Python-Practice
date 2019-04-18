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
import re
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
        self.start_offset = 20
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
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="
        url +=  str(self.start) + "&limit=" + str(self.start + self.start_offset)

        response = requests.get(url, headers={"user-agent": random.choice(self.user_agents)})
        print(url)
        if response.text == "[]":
            return
        self.jsonData(response.text)

    def jsonData(self, data):
        data = json.loads(data)

        # 影片排名
        rank_list = jsonpath.jsonpath(data, "$..rank")
        # 电影名称
        title_list = jsonpath.jsonpath(data, "$..title")
        # 电影封面
        cover_list = jsonpath.jsonpath(data, "$..cover_url")
        # 影片评分
        score_list = jsonpath.jsonpath(data, "$..score")
        # 电影类型
        types_list = jsonpath.jsonpath(data, "$..types")
        # 制片地区
        regions_list = jsonpath.jsonpath(data, "$..regions")
        # 上映时间
        release_list = jsonpath.jsonpath(data, "$..release_date")
        # 电影评论
        url_list = jsonpath.jsonpath(data, "$..url")

        for rank, title, cover, score, types, release, regions, url in zip(rank_list, title_list, cover_list, score_list, types_list, release_list, regions_list, url_list):
            self.item["rank"] = rank
            self.item["title"] = title
            self.item["cover"] = cover
            self.item["score"] = float(score)
            self.item["types"] = "/".join(types)
            self.item["release"] = release
            self.item["regions"] = "/".join(regions)
            self.item["url"] = int(re.findall(r".*?subject/(\d+)/", url)[0])
            self.writeData()

        self.start += self.start_offset
        time.sleep(random.randint(1, 2))
        # self.startWork()

    def writeData(self):  # 保存成json格式的
        content = json.dumps(self.item, ensure_ascii=False) + ",\n"  # 关闭默认转码为2进制
        with open("Douban.json", "a", encoding="utf-8") as rr:
            rr.write(content)

if __name__ == '__main__':
    work = DouBanSpider()
    work.startWork()