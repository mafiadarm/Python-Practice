#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Loffew'
"""
==============================
    Date:           07_30_2018  12:50
    File Name:      /SpiderWeb/chrome_headless
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    chrome是ChromeOptions里面增加“headless”，再用Chrome访问
==============================
"""

from selenium.webdriver import ChromeOptions, Chrome


def chrome(proxies=None):
    # 设置
    co = ChromeOptions()
    co.set_headless()  # 有直接设置的方法
    # co.add_argument('lang=zh_CN.UTF-8')  # 设置编码

    # 增加user-agent  移动版表格http://www.fynas.com/ua
    co.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"')

    # 禁止图片加载
    photo_check = {"profile.managed_default_content_settings.images": 2}
    co.add_experimental_option("prefs", photo_check)

    # 添加代理
    proxy = proxies
    dc = co.to_capabilities()  # 返回的是一个已经整理好的字典
    dc["proxy"] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "noProxy": None,
        "proxyType": "MANUAL",
        "class": "org.openqa.selenium.Proxy",
        "autodetect": False,
    }

    # 实例化，并加入设置
    driver = Chrome(
        chrome_options=co,
        # desired_capabilities=dc
    )
    driver.maximize_window()

    return driver


if __name__ == '__main__':
    url = "http://www.baidu.com"
    aha = chrome()

    try:
        visit = aha.get(url)
        test = aha.find_element_by_link_text("贴吧")
        print(test.text)
    except:
        print("error: !!!")
    finally:
        aha.close()

