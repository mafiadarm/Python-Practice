#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           09_25_2018  23:21
  File Name:      /Practice/get_data_from_taobao
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


def parse_page(title, price, sales, local):
    try:
        with open("月饼好不好吃.txt", "a", encoding="utf-8") as moon:
            for i in range(len(title)):
                cake = f"{title[i].text},{price[i].text},{sales[i].text[:-3]},{local[i].text.split(' ')[0]}\n"
                moon.write(cake)
    except:
        print("")

def from_selenium_get_html():
    # bro = webdriver.PhantomJS()
    bro = webdriver.Firefox()
    try:
        bro.get("http://www.taobao.com/")

        bro.find_element_by_xpath('//*[@id="q"]').send_keys("月饼")
        bro.find_element_by_id("q").send_keys(Keys.ENTER)

        for page in range(100):
            time.sleep(2)
            print(page)
            title = bro.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]//*[@class="row row-2 title"]/a')
            price = bro.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]//*[@class="price g_price g_price-highlight"]/strong')
            sales = bro.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]//*[@class="deal-cnt"]')
            local = bro.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]//*[@class="location"]')
            parse_page(title, price, sales, local)
            # 翻页的时候，需要把鼠标放在定位的元素上，有鼠标移入检测，或者使用屋头浏览器
            bro.find_element_by_link_text("下一页").click()

    finally:
        bro.quit()

if __name__ == '__main__':
    from_selenium_get_html()