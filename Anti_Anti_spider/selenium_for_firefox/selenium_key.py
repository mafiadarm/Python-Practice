#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           09_25_2018  14:41
  File Name:      /selenium_for_firefox/selenium_key
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)

driver.find_element_by_id('kw').send_keys('selenium')  #在搜索框中输入"selenium"
driver.find_element_by_id('kw').send_keys(Keys.SPACE)  #输入空格键
driver.find_element_by_id('kw').send_keys('python')  #在搜索框中输入"python"
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')  #输入Control+a模拟全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')  #输入Control+c模拟复制
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')  #输入Control+v模拟粘贴
driver.find_element_by_id('kw').send_keys(Keys.ENTER)  #输入回车代替点击搜索按钮

time.sleep(3)
driver.close()

#下面是一些常用的键盘事件：

# Keys.BACK_SPACE：回退键（BackSpace）
# Keys.TAB：制表键（Tab）
# Keys.ENTER：回车键（Enter）
# Keys.SHIFT：大小写转换键（Shift）
# Keys.CONTROL：Control键（Ctrl）
# Keys.ALT：ALT键（Alt）
# Keys.ESCAPE：返回键（Esc）
# Keys.SPACE：空格键（Space）
# Keys.PAGE_UP：翻页键上（Page Up）
# Keys.PAGE_DOWN：翻页键下（Page Down）
# Keys.END：行尾键（End）
# Keys.HOME：行首键（Home）
# Keys.LEFT：方向键左（Left）
# Keys.UP：方向键上（Up）
# Keys.RIGHT：方向键右（Right）
# Keys.DOWN：方向键下（Down）
# Keys.INSERT：插入键（Insert）
# DELETE：删除键（Delete）
# NUMPAD0 ~ NUMPAD9：数字键1-9
# F1 ~ F12：F1 - F12键
# (Keys.CONTROL, ‘a’)：组合键Control+a，全选
# (Keys.CONTROL, ‘c’)：组合键Control+c，复制
# (Keys.CONTROL, ‘x’)：组合键Control+x，剪切
# (Keys.CONTROL, ‘v’)：组合键Control+v，粘贴
