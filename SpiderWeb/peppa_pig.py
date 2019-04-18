#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           04_18_2019  17:04
  File Name:      /Python-Practice/peppa_pig
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
import re

from SpiderWeb.peppa_pig_link import link
from SpiderWeb.黑吧云点播 import main_small

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)

def start_project():
    """
        提取后批量下载，如果内存吃得消，尽管用线程池
        selenium可是很占内存的
    :return:
    """
    rule = re.compile(r'.*?href="(.*?.html).*?title="(第\d+集)"')
    result = rule.findall(link)
    for movie, movie_name in result:
        main_small(movie, movie_name)

def fix_error(file):
    """
        下载错误会被记录，提取记录，教它重新做人
        需要手动检查日志
    :param file:
    :return:
    """
    with open(file, "r", encoding="utf-8") as rr:
        fix = rr.readlines()

    for i in fix:
        movie, movie_name = i.split(" ")
        movie_name = movie_name.replace("\n", "")
        main_small(movie, movie_name)

if __name__ == '__main__':
    a = r"E:\GitHub\Python-Practice\SpiderWeb\error.log"
    fix_error(a)
