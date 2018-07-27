#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  11:34
  File Name:      /Anti_Anti_spider/HtmlDownload
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  爬取多个网站，进行数据汇总
  编码有不确定性，所以要用chardet来解析
==============================
"""

import logging
import requests
import chardet
import time

from proxy_pool.config import get_headers

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


class Downloader:
    """
    下载类，对url进行请求，返回文本数据
    """

    def download(self, url):
        print("Download:{}".format(url))  # 因为url在变化，所以要用异常处理
        r = requests.get(url, headers=get_headers(), timeout=10)
        # print(chardet.detect(r.content))  # 识别编码过程{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
        r.encoding = chardet.detect(r.content)["encoding"]  # 解对应编码
        if r.status_code == 200 or len(r.content) > 500:  # 如果访问成功
            return r.text  # 返回文本

    def try_download(self, url):
        try:
            if not self.download(url):
                raise ConnectionError
        except Exception as e:
            count = 0
            print("try again: ", e)
            while count < 3:
                time.sleep(5)
                self.download(url)
                count += 1


if __name__ == '__main__':
    Downloader.download("https://www.baidu.com")
