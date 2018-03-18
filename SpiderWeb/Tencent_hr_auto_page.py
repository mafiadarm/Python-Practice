#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           03_17_2018  20:37
  File Name:      /GitHub/tencent_hr
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - -
  Description:
  用xpath抓取数据
  xpath返回的是一个list
==============================
"""
import logging
import random
import json

import time
from lxml import etree

import requests

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


class TencentSpider:
    def __init__(self):
        self.next_url = "https://hr.tencent.com/position.php?&stat=#a0"
        USER_AGENTS = [
            'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36'
        ]
        self.headers = {
            "User-Agent": random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=5vee98k793c671i95cd5954n06;pgv_pvi=6839118848;pgv_si=s8673731584',
            'Host': 'hr.tencent.com',
            'Upgrade-Insecure-Requests': '1',
        }

    def start_work(self):
        item = {}
        response = requests.get(url=self.next_url, headers=self.headers)
        html = etree.HTML(response.text)
        self.next_url = "https://hr.tencent.com/" + "".join(html.xpath("//a[@id='next']/@href"))
        if self.next_url.endswith("javascript:;"):
            return

        node_list = html.xpath("//*[@class='even']|//*[@class='odd']")
        if not node_list:
            return

        for node in node_list:
            item["name"] = "".join(node.xpath(".//td[1]/a/text()"))
            item["detailLink"] = "".join(node.xpath(".//td[1]/a/@href"))
            item["positionInfo"] = "".join(node.xpath(".//td[2]/text()"))
            item["peopleNumber"] = "".join(node.xpath(".//td[3]/text()"))
            item["workLocation"] = "".join(node.xpath(".//td[4]/text()"))
            item["publishTime"] = "".join(node.xpath(".//td[5]/text()"))
            self.write_data(item)

        time.sleep(random.random())
        self.start_work()

    def write_data(self, item):
        content = json.dumps(item, ensure_ascii=False) + ",\n"
        with open("Tencent.json", "a", encoding="utf-8") as ff:
            ff.write(content)


if __name__ == '__main__':
    work = TencentSpider()
    work.start_work()
