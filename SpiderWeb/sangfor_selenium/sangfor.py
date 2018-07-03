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
    bro.find_element_by_xpath('//*[@onclick="opencat(cat102000,img102000);"]').click()  # 上网流量统计
    # bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[1]/a').click()  # 组流量排行
    bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[2]/a').click()  # 用户流量排行  使用


    # bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[3]/a').click()  # IP流量排行
    bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dd/a').click()  # 应用流量排行  使用


    bro.find_element_by_xpath('//*[@onclick="opencat(cat103000,img103000);"]').click()  # 上网行为统计
    # bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[1]/a').click()  # 组行为排行
    # bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[2]/a').click()  # 用户行为排行
    # bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[3]/a').click()  # IP行为排行
    bro.find_element_by_xpath('//*[@id="cat103000"]/dl/dt[4]/a').click()  # 应用类型排行    使用
==============================
"""
import time

import datetime
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author__ = 'Loffew'

def start():
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
    print("switch to first")
    bro.switch_to.frame(1)
    print("switch to second")
    # print(bro.page_source)
    # print(bro.find_element_by_class_name("wangguan").get_attribute("class"))

    element = (By.CLASS_NAME, "wangguan")
    WebDriverWait(bro, 20, 0.5).until(EC.presence_of_all_elements_located(element))

    # 点选表单
    bro.find_element_by_id("CollapsiblePanel5").click()

    bro.find_element_by_xpath('//*[@onclick="opencat(cat102000,img102000);"]').click()  # 上网流量统计
    bro.find_element_by_xpath('//*[@onclick="opencat(cat103000,img103000);"]').click()  # 上网行为统计

    bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dt[2]/a').click()  # 用户流量排行  使用

    # 点选收集内容范围
    bro.switch_to.parent_frame()
    bro.switch_to.frame("mainFrame")

    element = (By.ID, "stat_date_from")
    WebDriverWait(bro, 16, 0.5).until(EC.presence_of_all_elements_located(element))

    bro.find_element_by_id("stat_date_from").clear()
    bro.find_element_by_id("stat_date_from").send_keys(date)

    Select(bro.find_element_by_id("stat_date_type")).select_by_index(2)

    Select(bro.find_element_by_id("time_from_one")).select_by_index(8)
    Select(bro.find_element_by_id("time_to_one")).select_by_index(11)
    Select(bro.find_element_by_id("time_from_two")).select_by_index(13)
    Select(bro.find_element_by_id("time_to_two")).select_by_index(17)

    bro.find_element_by_id("stat_time_one").click()
    bro.find_element_by_id("stat_time_two").click()

    bro.find_element_by_id("place").clear()
    bro.find_element_by_id("place").send_keys("10")

    bro.find_element_by_id("query_2").click()

    element = (By.ID, "ctable")
    WebDriverWait(bro, 18, 0.5).until(EC.presence_of_all_elements_located(element))
    print("form is ok")

    table = []
    data_list = bro.find_elements_by_xpath('//*[@id="ctable"]/tbody/tr')
    data_list.pop(0)
    for tr in data_list:
        table.append(tr.text)

    table = [i.split(" ") for i in table]

    bro.close()

    into_excel(date+"用户流量排行", table)



def into_excel(name, table):
    # 写入excel
    workbook = xlsxwriter.Workbook(f'{name}.xlsx')
    worksheet = workbook.add_worksheet("information")

    for i, data in enumerate(table):
        for j, value in enumerate(data):
            print(i, j, value)
            worksheet.write(i, j, value)

    workbook.close()


if __name__ == '__main__':
    date = "2018-06-01"
    start()
