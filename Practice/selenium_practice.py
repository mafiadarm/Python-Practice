#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_14_2018  14:20
    File Name:      /GitHub/selenium_practice
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    用selenium 在百度搜索内容
==============================
"""

import logging
from selenium import webdriver

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

# 实例化
driver = webdriver.Firefox()
url = "https://www.baidu.com"
# 登陆网站
driver.get(url)
# 查找xpath，并发送内容
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python")
# 查找xpath，并点击
driver.find_element_by_xpath('//*[@id="su"]').click()

# 退出
driver.quit()  # driver.close()