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
    启动run[循环]
        开启线程池对已经有的ip池进行检测，并更新分数，检测完毕返回剩余总数
        如果总数小于2000，则启动爬虫程序
            开启线程池对页面进行爬取，每爬取一个页面，存一次数据到await
            爬取完毕，对已经爬取的ip进行检测
                如果可用，删除await中的此元素，增加到working
                间隔一天
==============================
"""
import logging

import time
from multiprocessing.dummy import Pool
from multiprocessing import Manager
from config import parser_list
from spider.HtmlDownload import Downloader
from spider.HtmlParser import Parser
from spider.check import recycle_check
from database.redis.Redis_save import RedisSet


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


class Crawl:
    """
    爬虫逻辑类
        从网页爬取ip:port
        把ip:port存入无需set
        从无序set检测，可用的放入有序并附分值
        循环检测有序池，如果总数量少于一定值，则启动爬虫
    """
    @staticmethod
    def thread_to_download(url, praser, par_dict, redis_to):
        response = Downloader().try_download(url)  # 返回的是url的text
        if response:
            proxy_list = praser.parse(response, par_dict)  # ["","",""]
            # 存入数据库预置点
            redis_to.sadd("await", *proxy_list)

    def crawl(self, url=None):
        """
        请求 解析页面
        把网站的url都放进列表，然后遍历后放进来[按每页]
        线程池操作：
            获取到的url，按每页的内容汇总后存入redis
        :return:
        """
        pool = Pool()
        rs = RedisSet().connect_pool()
        parser = Parser()
        for par_dict in parser_list:
            for url in par_dict["urls"]:
                pool.apply_async(self.thread_to_download, args=(url, parser, par_dict, rs))
        pool.close()
        pool.join()

        recycle_check(url, "await")

    def run(self):
        """
        循环检测数据库中可用代理数量，如果低于一定数量则启动爬虫程序，重新去爬取
        :return:
        """
        while 1:
            print("启动检测函数，等待处理")
            count = recycle_check()

            if count < 2000:
                print(f"当前可用代理数量为{count}, 小于2000, 启动爬虫程序")
                self.crawl()

            time.sleep(60*60*24)  # 间隔24小时


if __name__ == '__main__':
    queue = Manager().Queue()

