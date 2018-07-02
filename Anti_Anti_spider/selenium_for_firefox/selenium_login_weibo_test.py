#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           06_26_2018  20:55
  File Name:      /GitHub/selenium_login_weibo_test
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  使用firefox驱动和selenium实现模拟网页访问
  目标网页：https://weibo.com/
  找到元素 id = loginname 填入 账号
  找到元素 //*[@id="pl_login_form"]/div/div[3]/div[2]/div/input  填入密码
  过程中需要等待，直到这两个元素出现
  点击//*[@id="pl_login_form"]/div/div[3]/div[6]/a 进行登陆动作
  直到登陆页面的用户名元素出现，判断登陆成功
  打印cookies
==============================
"""
import random

import time

__author__ = 'Loffew'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def firefox_login():
    firefox = webdriver.Firefox()

    firefox.get(target_url)

    WebDriverWait(firefox, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(element_user))
    WebDriverWait(firefox, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(element_password))

    firefox.find_element_by_id("loginname").clear()
    firefox.find_element_by_id("loginname").send_keys(username)
    firefox.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
    firefox.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

    WebDriverWait(firefox, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(element_success_page))
    print(firefox.get_cookies())

    firefox.close()


def phantomjs_login():
    phantomjs_option = dict(DesiredCapabilities.PHANTOMJS)
    # phantomjs_option["phantomjs.page.settings.userAgent"] = random.choice(User_Agent_list)  # 加了头报错
    phantomjs_option["phantomjs.page.settings.loadImages"] = False
    phantomjs = webdriver.PhantomJS(desired_capabilities=phantomjs_option,)
    # phantomjs = webdriver.PhantomJS()

    # print(phantomjs_option)

    phantomjs.get(target_url)
    phantomjs.maximize_window()

    WebDriverWait(phantomjs, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(element_user))
    WebDriverWait(phantomjs, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(element_password))

    # print(phantomjs.page_source)
    name = phantomjs.find_element_by_id("loginname")
    name.clear()
    name.send_keys(username)

    word = phantomjs.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
    word.send_keys(password)

    phantomjs.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    # print(phantomjs.page_source)

    # WebDriverWait(phantomjs, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(element_success_page))
    print(phantomjs.get_cookies())

    cookies = {}
    for item in phantomjs.get_cookies():
        cookies[item.get("name")] = item.get("value")
        # print(item.get("name"), item.get("value"))
    # print(cookies)

    phantomjs.close()


if __name__ == '__main__':
    target_url = "https://weibo.com/"
    username = ""  # 只能是電話號碼，如果用郵箱，要把@轉碼
    password = ""
    element_user = (By.ID, "loginname")
    element_password = (By.XPATH, '//*[@id="pl_login_form"]/div/div[3]/div[2]/div/span')
    element_success_page = (By.XPATH, '//*[@id="v6_pl_rightmod_myinfo"]/div/div/div[2]/div/a[1]')

    # firefox_login()
    phantomjs_login()
