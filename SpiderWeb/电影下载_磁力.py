#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           01_13_2019  16:35
  File Name:      /Python-Practice/test
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import random
import time
from lxml import etree
import requests

class FromXGetDownload:
    def __init__(self):
        self.session = requests.Session()
        self.url = "http://cntorrentkitty.cc"
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

    def find_film_name(self, name):
        to_url = self.url + f"/tk/{name}/1-0-0.html"
        response = requests.get(to_url, headers={"user-agent": random.choice(self.user_agents)}, verify=False)
        url_etree = etree.HTML(response.content.decode())
        self.url_path = url_etree.xpath(r'//*[@class="list"]/p/a/@href')  # 这里如果返回的空，则需要重新获取
        # 如果没有获取到信息，而且没有返回没找到的信息则重新获取
        if not self.url_path and not url_etree.xpath(r'//*[@class="alert"]/text()'):  # 为什么是空的呢？因为有广告
            time.sleep(2)
            print("find_film_name again")
            self.find_film_name(name)

    def find_url_page(self, page_url):
        response = requests.get(page_url, headers={"user-agent": random.choice(self.user_agents)}, verify=False)
        url_etree = etree.HTML(response.content.decode())
        self.download_url = url_etree.xpath(r'//*[@class="dd magnet"]/a/@href')  # 这里如果返回的空，则需要重新获取
        if not self.download_url:
            time.sleep(2)
            print("find_url_page again")
            self.find_url_page(page_url)

    def find_download_url(self, name):
        self.find_film_name(name)
        container = []
        for x_url in self.url_path[:2]:
            time.sleep(1)
            page_url = self.url + x_url
            self.find_url_page(page_url)
            container.append(self.download_url[0])
        if not container:
            return "CAN NOT FIND"
        return container

if __name__ == '__main__':
    down = FromXGetDownload()
    url = down.find_download_url("081514_863")
    print(url)