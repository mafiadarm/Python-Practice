#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_22_2018  15:22
  File Name:      /Anti_Anti_spider/main
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""

from multiprocessing import Process
from server.flask_server import start_server
from spider.Html_Crawl import Crawl

if __name__ == '__main__':

    proxy_crawl = Process(target=Crawl.run)  # 不断检测已有的
    server = Process(target=start_server)  # web服务

    proxy_crawl.start()
    server.start()

    proxy_crawl.join()
    server.join()
