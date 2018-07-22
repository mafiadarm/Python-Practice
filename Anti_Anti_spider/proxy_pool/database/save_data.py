#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_21_2018  16:37
  File Name:      /Anti_Anti_spider/save_data
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
from .Mongo_Save import Mongo_Helper

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


def save_proxies(queue):
    """
    读取队列当中的代理，添加到数据库
    :param queue: 可用代理的队列
    :return:
    """
    while 1:
        try:
            proxy = queue.get(timeout=300)
            if proxy:
                Mongo_Helper().insert(proxy)
        except Exception as e:
            print("添加可用代理时发生错误：{}".format(e))