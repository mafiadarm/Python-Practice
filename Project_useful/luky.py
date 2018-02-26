# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_19_2018  14:24
   File Name:      /GitHub/luky
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:    查询一次，同时打开多个结果
==============================
"""
import logging
import requests, sys, webbrowser, bs4, os

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def lukyDog():
    """
    复制要查询的内容
    为每个查询到的结果打开一个浏览器选项卡
    """
    print("Googling....")
    res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    linkElems = soup.select("r. a")  # 查找r类的元素中<a>元素

    numOpen = min(5, len(linkElems))  # 限制最多打开5个
    for i in range(numOpen):
        webbrowser.open("http://google.com" + linkElems[i].get("href"))


def photo():
    """
    进入http://xkcd.com
    下载漫画图片
    转到前一页，重复动作，直到第一张
    """
    url = "http://xkcd.com"
    os.makedirs("xkcd", exist_ok=True)  # exist_ok= 防止该文件夹存在时，抛出报错
    while not url.endswith("#"):
        # 下载文件
        print("Downloading page %s" % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        # 找到图的url
        comicElem = soup.select("#comic img")
        if comicElem is []:
            print("没找到comic image")
        else:
            comicUrl = "http:" + comicElem[0].get("src")
            # 下载图片
            print("Downloading image %s" % comicUrl)
            req = requests.get(comicUrl)
            req.raise_for_status()
            # 保存图片
            with open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb") as imageFile:  # b 多媒体必用
                imageFile.write(req.content)  # 图片用content
            # 找到Prev按钮
            prevLink = soup.select("a[rel='prev']")[0]
            url = "http://xkcd.com" + prevLink.get("href")

