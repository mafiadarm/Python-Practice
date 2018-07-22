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

from multiprocessing import Process, Manager
from proxy_pool.server.flask_server import start_server
from proxy_pool.spider.Html_Crawl import start_crawl
from proxy_pool.database.save_data import save_proxies

if __name__ == '__main__':
    queue1 = Manager().Queue()  # 所有的代理队列
    queue2 = Manager().Queue()  # 可用代理的对立
    proxy_crawl = Process(target=start_crawl, args=(queue1, queue2))  # 不断检测
    server = Process(target=start_server)  # web服务
    save_proxy = Process(target=save_proxies, args=(queue2,))

    proxy_crawl.start()
    server.start()
    save_proxy.start()

    proxy_crawl.join()
    save_proxy.join()
    server.join()
