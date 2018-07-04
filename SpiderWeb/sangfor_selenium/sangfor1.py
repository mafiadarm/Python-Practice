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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from write_to_excel import into_excel

__author__ = 'Loffew'


def into_page(date, bro):
    bro.switch_to.default_content()

    bro.switch_to.frame(0)
    print("switch to first")
    bro.switch_to.frame(1)
    print("switch to second")

    bro.find_element_by_xpath('//*[@id="cat102000"]/dl/dd/a').click()  # 应用流量排行  使用

    # 点选收集内容范围
    bro.switch_to.parent_frame()
    bro.switch_to.frame("mainFrame")

    element = (By.ID, "stat_date_from")
    WebDriverWait(bro, 16, 0.5).until(EC.presence_of_all_elements_located(element))

    bro.find_element_by_id("stat_date_from").clear()
    bro.find_element_by_id("stat_date_from").send_keys(date)
    bro.find_element_by_id("time_from_two").click()

    Select(bro.find_element_by_id("stat_date_type")).select_by_index(2)

    Select(bro.find_element_by_id("time_from_one")).select_by_index(8)
    Select(bro.find_element_by_id("time_to_one")).select_by_index(18)

    bro.find_element_by_xpath('//*[@class="table_new"]/table/tbody/tr/td/input[@value="app"]').click()

    bro.find_element_by_id("place").clear()
    bro.find_element_by_id("place").send_keys("30")

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

    into_excel(date+"应用流量排行", table)
    return bro


if __name__ == '__main__':
    pass