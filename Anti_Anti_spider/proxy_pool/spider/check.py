#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_21_2018  19:18
  File Name:      /Anti_Anti_spider/check
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
import requests
import time
from multiprocessing.pool import ThreadPool
from proxy_pool.database.Mongo_Save import Mongo_Helper

import urllib3

from proxy_pool import config

urllib3.disable_warnings()


def mongo_proxy_check(proxy_list, proxies_set):
    for proxy in proxy_list:
        proxy_dict = {"http": f"http://{proxy[0]}:{proxy[1]}", "https": f"https://{proxy[0]}:{proxy[1]}"}
        result = mongo_check(proxy_dict)
        if not result:
            if proxy[2] < 1:
                Mongo_Helper().delete({"ip": proxy[0], "port": proxy[1]})
            else:
                score = proxy[2] - 1
                Mongo_Helper().update({"ip": proxy[0], "port": proxy[1]}, {"score": score})
        else:
            proxies_set.add(result)


def threading_check_proxy(proxy_list, queue):
    pool = ThreadPool()
    for proxy in proxy_list:
        proxies = {"http": f"http://{proxy['ip']}:{proxy['port']}", "https": f"http://{proxy['ip']}:{proxy['port']}"}
        # t = threading.Thread(target=bd_check, args=(i,))  # 线程方法
        print("开始检测", proxies)
        pool.apply_async(bd_check, args=(proxy, proxies, queue))
    pool.close()
    pool.join()


def bd_check(proxy, proxies, queue, url=None):
    """
    检测代理是否可用
    :param url:
    :return:
    """
    if not url:
        url = "https://www.baidu.com"
    try:
        start_time = time.time()
        res = requests.get(url=url, headers=config.get_headers(), proxies=proxies, verify=False)
        if res.status_code == 200:
            speed = round(time.time() - start_time, 3)
            print(f"代理 {proxies} 可用，响应时间为 {speed}")
            proxy["speed"] = speed
            queue.put(proxy)
        else:
            speed = -1
    except Exception:
        speed = -1
        print(f"错误：代理 {proxies} 不可用")

    return speed


def mongo_check(proxies, url=None):
    """
    检测代理是否可用
    :param proxies:
    :param url:
    :return:
    """
    if not url:
        url = "https://www.baidu.com"
    if not proxies:
        proxies = {}
    try:
        res = requests.get(url=url, headers=config.get_headers(), proxies=proxies, verify=False)
        if res.status_code != 200:
            return False
        return True
    except Exception:
        return False
