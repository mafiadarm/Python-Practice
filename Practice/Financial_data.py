#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_13_2018  10:27
    File Name:      /GitHub/Financial_data
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    page is tushare
==============================
"""

import logging
import tushare

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

pp_dbg(tushare.get_today_all())
