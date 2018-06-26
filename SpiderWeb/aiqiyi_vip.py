#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           06_11_2018  14:12
    File Name:      /GitHub/aiqiyi_vip
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    通过旋风视频VIP解析网站来拿到实际播放地址，并且下载
==============================
"""

import logging

import time
import requests
import re
from urllib.parse import *


__author__ = 'Loffew'

# logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

"""
爱奇艺的vip，直接破有法律风险，刚好有个解析网站，可以获取实际播放地址
直接使用http://api.xfsub.com/index.php?url=<爱奇艺的vip播放地址>
"""