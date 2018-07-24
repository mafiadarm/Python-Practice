#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_14_2018  21:35
  File Name:      /Anti_Anti_spider/working_on_web
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  pip install pyspider
  cmd启动服务 pyspider
  浏览器打开localhost:5000[看提示]
==============================
"""
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)
    