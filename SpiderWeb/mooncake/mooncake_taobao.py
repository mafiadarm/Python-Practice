#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           09_24_2018  19:24
  File Name:      /Practice/mooncake_taobao
  Creat From:     PyCharm
  Python version: 3.7.0
- - - - - - - - - - - - - - - 
  Description:
  工具&模块：
工具：Python3.7+Sublime Text
模块：requests、jieba、matplotlib、wordcloud、imread、pandas、numpy 等。
目的主要是通过对数据的分析，来看看不同关键词word对应的sales的统计、月饼价格以及销量的分布情况、以及不同省份的月饼销量情况。
==============================
"""
import random
import re
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

__author__ = 'Loffew'


def parse_page(html):
    print("from html parse page")
    try:
        tlt = re.findall(r'"raw_title":".*?"', html)  # 标题
        plt = re.findall(r'"view_price":".*?"', html)  # 单价
        loc = re.findall(r'"item_loc":".*?"', html)  # 区域
        sal = re.findall(r'"view_sales":".*?"', html)  # 销售量

        print(plt)
        with open("月饼好不好吃.txt", "a", encoding="utf-8") as moon:
            for i in range(len(plt)):
                title = eval(tlt[i].split(":")[1])
                price = eval(plt[i].split(":")[1])
                location = eval(loc[i].split(":")[1])
                location = location.split(" ")[0]
                sales = eval(sal[i].split(":")[1])
                sales = re.match(r"\d+", sales).group(0)

                cake = f"{title},{price},{sales},{location}\n"
                moon.write(cake)
    except:
        print(html)


def get_html(url):
    try:
        res = requests.get(url, timeout=30)
        res.raise_for_status()  # 返回状态
        res.encoding = res.apparent_encoding  # 自动识别编码,大概率能中
        return res.text
    except Exception as ex:
        print(f"{url} error:", ex)
        return ""


def main():
    """
    暴力爬不实际，获取快，但是几率性返回数据
    :return:
    """
    # https://s.taobao.com/search?q=月饼&s=22
    goods = "月饼"
    depath = 100  # 淘宝只支持100页
    start_url = "https://s.taobao.com/search?q=" + goods
    for i in range(1, depath):
        try:
            url = start_url + "&s=" + str(44 * i)
            print(url)
            html = get_html(url)
            parse_page(html)
        except:
            continue






if __name__ == '__main__':
    from_selenium_get_html()

    