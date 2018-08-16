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

from config import get_headers

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


class Downloader:
    """
    下载类，对url进行请求，返回文本数据
    """
    @staticmethod
    def download(url):
        print("Download:{}".format(url))  # 因为url在变化，所以要用异常处理
        r = requests.get(url, headers=get_headers(), timeout=10)
        r.encoding = chardet.detect(r.content)["encoding"]  # 解对应编码
        if r.status_code == 200 or len(r.content) > 500:  # 如果访问成功
            return r.text  # 返回文本

    def try_download(self, url, flag=0):
        """
        尝试连接3次需要爬取的页面，超过则放弃
        :param flag:
        :param url:
        :return:
        """
        if flag == 3:
            return
        try:
            text = self.download(url)
            if not text:
                raise ConnectionError
            else:
                return text
        except Exception as e:
            print("try again: ", e)
            time.sleep(2)
            flag += 1
            self.try_download(url, flag)


if __name__ == '__main__':
    Downloader().download("https://www.baidu.com")
