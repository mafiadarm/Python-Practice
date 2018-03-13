#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_13_2018  11:17
    File Name:      /GitHub/sound_to_text
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import requests

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def get_ip():
    params = {
        'appkey': 'd60a836ce08f426a96f73af6962a68d3',
        'count': 20,
        'expiryDate': 0,
        'format': 1
    }
    url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs'

    r = requests.get(url=url, params=params)
    r.encoding = 'utf-8'
    print(r)
    print(r.text)
    print(r.json())


if __name__ == '__main__':
    get_ip()
