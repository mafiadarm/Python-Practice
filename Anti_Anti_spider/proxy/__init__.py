#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  12:20
  File Name:      /Anti_Anti_spider/__init__
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)
    