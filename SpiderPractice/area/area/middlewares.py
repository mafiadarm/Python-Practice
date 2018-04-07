# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import scrapy
from scrapy import signals
from selenium import webdriver
import time


class AreaSpiderMiddleware(object):
    """
    因为在spider里面，只有第一个页面是静态的，使用中间件对后面的静态页面进行处理
    在不想弄js这种很麻烦的东西的时候，使用中间件来处理源码
    这个中间件可以直接使用，代替downloader
    """
    def process_request(self, request, spider):
        self.driver = webdriver.Firefox()
        if request.url != 'https://www.aqistudy.cn/historydata/':
            self.driver.get(request.url)
            time.sleep(1.5)
            html = self.driver.page_source
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html.encode("utf-8"), encoding="utf-8", request=request)