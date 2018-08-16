#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

__author__ = 'Loffew'
"""
==============================
    Date:           08_01_2018  16:24
    File Name:      /SpiderWeb/app1_search_data
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    主入口为百度查询：国家食品药品监督管理局数据查询 href:...
    连续：name=PL_MENU_NAME 医疗器械 @href
    连续：re.compile('href="(.*?国产器械.*?)"')

==============================
"""

from selenium.webdriver import ChromeOptions, Chrome, Ie
from selenium.webdriver.common.action_chains import ActionChains  # 用于拖拽的鼠标动作

def chrome(proxies=None):
    # 设置
    co = ChromeOptions()
    co.set_headless()  # 有直接设置的方法
    # co.add_argument('lang=zh_CN.UTF-8')  # 设置编码

    # 增加user-agent  移动版表格http://www.fynas.com/ua
    co.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"')

    # 禁止图片加载
    # photo_check = {"profile.managed_default_content_settings.images": 2}
    # co.add_experimental_option("prefs", photo_check)

    # 实例化，并加入设置
    driver = Chrome(
        # chrome_options=co,
        # desired_capabilities=dc
    )
    driver.maximize_window()

    return driver


def app():
    driver = chrome()
    try:
        # driver.get("http://www.baidu.com")
        # driver.find_element_by_id("kw").send_keys("国家食品药品监督管理局数据查询")
        # driver.find_element_by_id("su").click()
        # time.sleep(3)
        # driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
        # time.sleep(3)
        # # 获取所有窗口
        # all_windows = driver.window_handles
        # # 切换过去
        # driver.switch_to.window(all_windows[1])
        # time.sleep(3)
        # driver.find_element_by_xpath('//*[@id="BOC_NAVIGATOR_UL"]/table/tbody/tr/td[7]/li/a').click()
        # time.sleep(3)
        # driver.find_element_by_xpath('//div[@class="new20116_erji_font2"][contains(text(), "企业查询")]').click()
        # driver.find_element_by_xpath('//*//a[contains(text(), "国产器械")]').click()
        # # 以上从百度入口进去，因为有检测，反而打不开，而直接从入口进去，却直接能打开，如下：

        driver.get("http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=26&tableName=TABLE26&title=%B9%FA%B2%FA%C6%F7%D0%B5&bcId=118103058617027083838706701567")
        time.sleep(3)
        tag = driver.find_element_by_xpath('//*[@id="content"]/div/table[2]/tbody/tr[1]//a')
        ActionChains(driver).move_to_element(tag).click().perform()
        # driver.find_element_by_xpath('//*[@id="content"]/div/table[2]/tbody/tr[1]//a').click()
        print(driver.page_source)
        time.sleep(10)
    finally:
        print(111)
        # driver.quit()
if __name__ == '__main__':
    app()