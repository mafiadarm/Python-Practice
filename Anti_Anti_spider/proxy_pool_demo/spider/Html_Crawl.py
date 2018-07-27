#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  12:07
  File Name:      /Anti_Anti_spider/Html_Crawl
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging

import time

from multiprocessing import Manager
from proxy_pool.config import parser_list
from proxy_pool.spider.HtmlDownload import Downloader
from proxy_pool.spider.HtmlParser import Parser
from proxy_pool.spider.check import threading_check_proxy, mongo_proxy_check
from proxy_pool.database.save_data import save_proxies
from proxy_pool.database.Mongo_Save import Mongo_Helper


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def start_crawl(queueu1, queue2):
    crawl = Crawl(queue1, queue2)
    crawl.run()



class Crawl:
    """
    爬虫逻辑类
    """
    proxies = set()

    def __init__(self, queue1, queue2):
        self.queue1 = queue1  # 所有代理
        self.queue2 = queue2  # 有效代理

    def run(self):
        while 1:
            self.proxies.clear()
            print("启动检测函数，等待处理")
            proxy_list = Mongo_Helper().select()  # 获取当前数据库当中所有的代理
            mongo_proxy_check(proxy_list, self.proxies)
            if len(self.proxies) < 20:
                print(f"当前可用代理数量为{len(self.proxies)}, 小于20, 启动爬虫程序")
                for parser in parser_list:
                    self.crawl(parser)
            time.sleep(60)

    def crawl(self, parser):
        """
        请求 解析页面
        把网站的url都放进列表，然后遍历后放进来
        :return:
        """
        p = Parser()
        for url in parser["urls"]:
            response = Downloader().download(url)  # 返回的是url的text
            if response:
                proxy_list = p.parse(response, parser)
                self.save(proxy_list)

    def save(self, proxy_list):
        """
        字符串形式保存，并且保存到公用集合里面
        :param proxy_list:
        :return:
        """
        threading_check_proxy(proxy_list, self.queue2)
        # for proxy in proxy_list:
        #     proxy_str = "{}:{}".format(proxy["ip"], proxy["port"])
        #     # print(proxy)
        #
        #     if proxy_str not in self.proxies:
        #         self.proxies.add(proxy_str)
        #
        #         while True:  # 用队列？？
        #             if self.queue1.full():
        #                 time.sleep(1)
        #             else:
        #                 self.queue1.put(proxy)
        #                 break


if __name__ == '__main__':
    queue1 = Manager().Queue()
    queue2 = Manager().Queue()
    c = Crawl(queue1, queue2)
    for par_dict in parser_list:
        c.crawl(par_dict)
    save_proxies(queue2.get())
