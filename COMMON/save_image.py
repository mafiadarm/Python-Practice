#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           01_09_2019  13:38
  File Name:      /Python-Practice/save_image
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import requests

HEADERS = {}

def save_img(self, name, url):
    try:
        response = requests.get(url, headers=HEADERS, stream=True, timeout=10)
    except requests.ConnectionError:  # requests.ConnectTimeout被包含在里面
        print("图片无法下载")
        return
    except requests.exceptions.ReadTimeout:
        print("超时")
        return

    name = name.replace("*", "").replace("?", "").replace("|", "")

    try:
        # 保存图片
        with open(name, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        print(name, "is ok")
    except OSError:
        print("OSError", name, url)
        pass
    