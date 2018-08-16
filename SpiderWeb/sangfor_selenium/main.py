#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_04_2018  11:21
    File Name:      /GitHub/main
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import sangfor
import sangfor1
import sangfor2
import sangfor3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def start():
    bro = webdriver.Ie()

    bro.get("http://10.0.10.15:8888")

    element = (By.ID, "button")
    WebDriverWait(bro, 10, 0.5).until(EC.presence_of_all_elements_located(element))

    bro.find_element_by_xpath('//*[@id="login_user"]').clear()
    bro.find_element_by_xpath('//*[@id="login_user"]').send_keys("admin")
    bro.find_element_by_xpath('//*[@id="login_password"]').send_keys("admin")
    bro.find_element_by_xpath('//*[@id="button"]').click()

    element = (By.NAME, "a")
    WebDriverWait(bro, 10, 0.5).until(EC.presence_of_all_elements_located(element))

    bro.switch_to.frame(0)
    print("switch to first")
    bro.switch_to.frame(1)
    print("switch to second")

    element = (By.CLASS_NAME, "wangguan")
    WebDriverWait(bro, 10, 0.5).until(EC.presence_of_all_elements_located(element))

    # 点选表单
    bro.find_element_by_id("CollapsiblePanel5").click()

    bro.find_element_by_xpath('//*[@onclick="opencat(cat102000,img102000);"]').click()  # 上网流量统计
    bro.find_element_by_xpath('//*[@onclick="opencat(cat103000,img103000);"]').click()  # 上网行为统计

    return bro


if __name__ == '__main__':

    date_list = [
        "2018-07-01"
    ]

    page_list = [
        sangfor.into_page,
        sangfor1.into_page,
        sangfor2.into_page,
        sangfor3.into_page
    ]

    brow = start()
    try:
        for page in page_list:
            for date in date_list:
                page(date, brow)
    finally:
        brow.close()




