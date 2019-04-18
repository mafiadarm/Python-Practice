#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           01_09_2019  12:15
  File Name:      /Python-Practice/萌鸡小队第二季
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - -
  Description:
==============================
"""
import logging
import requests
import re
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import unquote

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)

def selenium_to_get_cut_url(url):
    find_url = webdriver.Chrome()  # 构建一个模拟器
    try:
        find_url.get(url)  # 获取这个url
        find_url.switch_to.frame(1)  # 这是第一层iframe
        find_url.switch_to.frame(0)  # 这是第二层iframe
        get_url = find_url.find_element_by_xpath(r'//*[@id="ckplayer_a1"]/param[7]/@value')
        get_url = unquote(get_url)
        re_get_url = re.findall(r"f=https://api.bbbbbb.me/ckplayer/m3u8.swf&a=(.*?)&c=\d+&s=\d+&lv=\d+&p=\d+&v=\d+&b=\d+&e=\d+&my_title=null", get_url)[0]  # 正则取出来
    finally:
        find_url.quit()
    return re_get_url


url_enter = "http://m.02x.net.cn/gq/mengjixiaoduidierji/"
url_head = "http://m.02x.net.cn"
session = requests.Session()

response = requests.get(url_enter)
html_to_xpath = etree.HTML(response.content)
items = html_to_xpath.xpath('//*[@id="vlink_1"]/ul/li/a/@href')
for url in items:
    # url = items[0]  # 测试的时候就一个一个的来
    url_get_flv = url_head + url
    file_name = re.findall(r".*?-(\d+-\d+)", url)[0]
    cut_url = selenium_to_get_cut_url(url_get_flv)  # 从selenium获取链接
    cut_response = requests.get(cut_url)  # 获取到切割的数据，再做数据处理
    cut_content = cut_response.content
    # 做文本处理
    ss = re.findall(r"(#.*?,|#.*?[\d\n]+)", cut_content)
    for i in set(ss):
        cut_content = re.sub(i, "", cut_content)
    url_list = cut_content[2:].replace("\n", " ").split(" ")
    # 拼接url，访问并返回数据流进行保存
    with open(file_name, "wb") as ww:
        for last_url in url_list:
            response = requests.get(url_head + last_url, stream=True, timeout=10)
            for block in response.iter_content(1024):
                if not block:
                    break
                ww.write(block)