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
  检查的目的是确认数据库里面有足够的代理
  同时循环检测代理是否依然可用，于是纳入分数
        常规检测 对应www.baidu.com
        预置检测 对应准备爬取的网站
==============================
"""
import requests
import time
from multiprocessing.pool import ThreadPool
import urllib3
import config
from database.redis.Redis_save import RedisSet

urllib3.disable_warnings()


def change_score(redis_to, ip_port, zname, speed, flag):
    ip, port, *_ = ip_port.split(":")
    if flag:
        if zname == "working":
            score = redis_to.zscore(zname, ip_port)
            point, _ = str(score).split(".")
            redis_to.add_to("zadd", zname, -10, ip_port)  # 旧值覆盖
            # 制造分值格式为 [点数.速度]
            redis_to.add_to("zadd", zname, float(".".join([point + 1, speed])), ":".join([ip, port]))  # 新值增加
        elif zname == "await":
            # 如果是待用值，则加入working
            redis_to.add_to("zadd", "working", float(".".join([10, speed])), ":".join([ip, port]))
            redis_to.pool.srem("srem", zname, ip_port)
    else:
        if zname == "working":
            redis_to.supdate("zincrby", zname, -1, ip_port)  # 原有分数-1


def check_proxy(redis_to, ip_port, zname, url=None):
    if not url:
        url = "https://www.baidu.com"

    ip, port, *_ = ip_port.split(":")
    proxies = {"http": f"http://{ip}:{port}", "https": f"http://{ip}:{port}"}

    start_time = time.time()
    try:
        res = requests.get(url=url, headers=config.get_headers(), proxies=proxies, verify=False)
        if res.status_code == 200:
            # speed = round(time.time() - start_time, 3)
            speed = time.time() - start_time
            print(f"响应时间为 {speed}，可用代理{proxies}")
            change_score(redis_to, ip_port, zname, speed, 1)
    except Exception:
            change_score(redis_to, ip_port, zname, 1001, 0)


def recycle_check(url=None, zname=None):
    """
    :param url: 代理将要访问的url目标
    :param zname:  数据库key-name
    :return:
    """
    global check_list
    redis_to = RedisSet()
    pool = ThreadPool()

    if not zname:
        zname = "working"
        check_list = redis_to.squery("zrange", zname, start=0, end=-1)
    elif zname == "await":
        check_list = redis_to.pool.smembers(zname)

    for ip_port in check_list:

        print("开始检测", ip_port)
        pool.apply_async(check_proxy, args=(redis_to, ip_port, zname, url))

    if zname == "working":
        redis_to.sdelete("delete", zname, -10, -7)
        return redis_to.squery("zcard", zname)


if __name__ == '__main__':
    pass