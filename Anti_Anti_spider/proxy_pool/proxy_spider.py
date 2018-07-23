#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  10:51
  File Name:      /Anti_Anti_spider/pachong
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  高并发的时候，网站会对ip进行封杀，这个时候就需要ip代理进行访问
  此动作分为几个部分
  1 爬虫部分
        从各大代理网站抓取免费的代理进行测试
  2 数据存储
        储存可用的代理地址
  3 调度
        控制，检测已有的IP地址
  4 api接口（web页面）
        数据库中的数据展示[使用flask即可]

  ps: 可以以pool池里面的ip做代理继续爬取ip，用线程池快速爬取与验证，周期性检测
        以时间为周期
        以代理池的有效ip存有量为周期
      ip的位置 可以用ipip的api，或者纯真IP数据库
      考虑存活率问题，所以要使用之前再做一次批量测试
==============================
"""

import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)
    