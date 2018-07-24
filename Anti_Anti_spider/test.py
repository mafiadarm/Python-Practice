#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  9:11
  File Name:      /Anti_Anti_spider/test
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  这是一个不正经的网站
==============================
"""
import logging
import json
import requests

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


keyword = "蜘蛛侠"

params = {
    "request_type": "search",
    "keywords": keyword,
    "device_id": "26d5213d-9bb9-9ae9-84ea-716caf704404",
    "page": 1,
}
rr = requests.get(url="https://www.soucili.net/request/?", params=params)
jj = rr.content.decode()
ee = json.loads(jj)["videos"]
for i in ee:
    print(i["file_name"], i["moc"], i["file_size"])

