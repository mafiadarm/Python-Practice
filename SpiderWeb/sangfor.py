#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_02_2018  15:58
    File Name:      /GitHub/sangfor
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author__ = 'Loffew'



bro = webdriver.Ie()
bro.get("http://10.0.10.15:8888")
# bro.find_element_by_link_text("详细信息").click()
# bro.find_element_by_link_text("转到此网页(不推荐)").click()

element = (By.ID, "button")
WebDriverWait(bro, 20, 0.5).until(EC.presence_of_all_elements_located(element))

bro.find_element_by_xpath('//*[@id="login_user"]').clear()
bro.find_element_by_xpath('//*[@id="login_user"]').send_keys("admin")
bro.find_element_by_xpath('//*[@id="login_password"]').send_keys("admin")
bro.find_element_by_xpath('//*[@id="button"]').click()

element = (By.NAME, "a")
WebDriverWait(bro, 20, 0.5).until(EC.presence_of_all_elements_located(element))

bro.switch_to.frame(0)
print("switch to a")
bro.switch_to.frame(1)
print("switch to 1")
# print(bro.page_source)
# print(bro.find_element_by_class_name("wangguan").get_attribute("class"))

element = (By.CLASS_NAME, "wangguan")
WebDriverWait(bro, 20, 0.5).until(EC.presence_of_all_elements_located(element))

bro.find_element_by_id("CollapsiblePanel5").click()
print("点开统计")

bro.find_element_by_xpath('//*[@onclick="opencat(cat102000,img102000);"]').click()  # 上网流量统计
bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[1]/a').click()  # 组流量排行
bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[2]/a').click()  # 用户流量排行
bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[3]/a').click()  # IP流量排行
bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[4]/a').click()  # 应用流量排行

bro.find_element_by_xpath('//*[@onclick="opencat(cat103000,img103000);"]').click()  # 上网行为统计
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[1]/a').click()  # 组行为排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[2]/a').click()  # 用户行为排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[3]/a').click()  # IP行为排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[4]/a').click()  # 应用类型排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[5]/a').click()  # URL排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[6]/a').click()  # 阻断动作分布
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[7]/a').click()  # 外发文件用户排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[8]/a').click()  # 热门论坛排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[9]/a').click()  # 论坛热帖排行
bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dd/a').click()  # 手机验证活跃用户排行




