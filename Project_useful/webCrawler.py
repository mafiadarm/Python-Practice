# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_18_2018  15:12
   File Name:      /GitHub/webCrawler
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:    学习从网页抓取
   web 初学者指南：
   http://htmldog.com/guides/html/beginner/
   https://www.codecademy.com/tracks/web
   https://developer.mozilla.org/en-US/docs/Learn/HTML
==============================
"""

__author__ = 'Loffew'

import lxml as lxml
import re
import webbrowser
import requests
import bs4
import selenium
import pyperclip
import sys
import logging
# logging.basicConfig(filename="logging.txt", level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

# html.parser lxml
# webbrowser.open("https://www.baidu.com")  # 直接打开一个页面 唯一作用

# if len(sys.argv) > 1:
#     address = " ".join(sys.argv[1:])
# else:
#     address = pyperclip.paste()
#
# webbrowser.open("=https://www.google.com/maps/place" + address)
'''
url_t = "http://www.gutenberg.org/cache/epub/1112/pg1112.txt"
res = requests.get(url_t)
try:
    res.raise_for_status()  # 确认下载完成，True什么都不会发生，False报错，可以用try来包裹
except Exception as exc:
    print(exc)  # 如果报错，就打印错误
print(res.status_code == requests.codes.ok)  # 确认状态码是ok
print(len(res.text))  # 查看文件有多大
print(res.text[:250])  # 截取一部分内容看
# 保存到文件
allText = len(res.text)
with open("RomeoAndJuliet.txt", "wb") as file:
    for chunk in res.iter_content(allText):  # 10W字节，实际上可以用len(res.text)的值
        file.write(chunk)  # write()返回一共获取了多少数据，剩下多少
'''
# url_bs = "https://nostarch.com"  # 有验证码反爬
# res_bs = requests.get(url_bs)
# res_bs.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res_bs.text)
# print(type(noStarchSoup))
# print(noStarchSoup)

# exampleFile = open("example.html", encoding="utf-8")
# exampleFile.readlines()
# exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
# logging.debug(type(exampleSoup))
# exampleFile.close()
#
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
# elems = exampleSoup.select("#author")
# logging.debug(elems)
#
# pElem = exampleSoup.select("p")
# print(str(pElem))
# print(pElem[0].getText())
#
# soup = bs4.BeautifulSoup(open("example.html", encoding="utf-8"), "html.parser")
# spanElem = soup.select("span")[0]
# logging.debug(spanElem.get("id"))
# logging.debug(spanElem.get("some_nonexistent_addr") is None)
# logging.debug(spanElem.attrs)

# 以下实例 说明BeautifulSoup用法[根据标签获取内容][定位][js里面无法定位]
html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body> 
<p class="title"><b>The Dormouse's story</b></p> 
<p class="story">Once upon a time there were three little sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
<a href="http://example.com/elsie" class="sis" id="link1">Elsie</a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p> 
<p class="story">...</p>
</body>
'''
# soup = bs4.BeautifulSoup(html_doc, "html.parser")
# logging.debug(soup)

# print(soup.find_all(re.compile("t")))
# print(soup.find_all(["a", "b"]))
# print(soup.find_all("a", class_="sister"))
# print(soup.find_all(text=re.compile("The")))

# def has_tag(tag):  # 匹配树[所有的]
#     return tag.has_attr("class") and tag.has_attr("id")
# print([tag.name for tag in soup.find_all(has_tag)])

# print(soup.select("#link3"))
# print(soup.select("a[href]"))
# print(soup.select("[href]"))

# for tag in soup.select("a"):
#     print(tag["href"])
# print(soup.get_text())


# bs4,pyv8,pyquery,xpath

# xpath 定位元素
# // 全文搜索
# @  取属性

# from lxml import etree
# /html/body/div/div这样写定位，一定不会出错，但是很麻烦
# tree = etree.HTML(html_doc)
# print(tree.xpath("/html")[0].text)
# print(tree.xpath("//a/@href"))
# print(tree.xpath("//a/@id"))
# print(tree.xpath('//a[@class="sis"]')[0].text)

# requests ISO 编码还是解码，要先看内容
# response = request.encode(UTF-8)
# a = "a"
# b = b"b"
# a.encode()
# b.decode()