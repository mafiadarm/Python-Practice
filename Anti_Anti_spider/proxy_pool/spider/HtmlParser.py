#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  11:35
  File Name:      /Anti_Anti_spider/HtmlParser
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  解析地址，需要检测 ip + 端口 响应速度 等等
==============================
"""
import logging
import re
from lxml import etree
from proxy_pool.address.ip_address import ipip_get_add

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


class Parser:
    def __init__(self):
        self.ip_addr = ipip_get_add

    def parse(self, response, parser):
        """
        :param response: 文本数据
        :param parser: 解析的方式
        :return:
        """
        if parser["type"] == "xpath":
            return self.xpath_parser(response, parser)
        if parser["type"] == "re":
            return self.re_parser(response, parser)

    def xpath_parser(self, response, parser):
        """
        针对xpath
        :param response:
        :param parser:
        :return:
        """
        proxy_list = []
        soup = etree.HTML(response)
        items = soup.xpath(parser["pattern"])  # xpath路径解析以实际打印出来的为准
        for item in items:
            ip = item.xpath(parser["position"]["ip"])[0].text
            port = item.xpath(parser["position"]["port"])[0].text
            addr = self.ip_addr(ip)
            proxy = {"ip": ip, "port": port, "addr": addr}
            proxy_list.append(proxy)

        return proxy_list

    def re_parser(self, response, parser):
        """
        针对正则表达式
        :param response:
        :param parser:
        :return:
        """
        pass
