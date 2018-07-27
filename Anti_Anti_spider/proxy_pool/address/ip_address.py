#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  20:02
  File Name:      /Anti_Anti_spider/ip_address
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  使用的ipip的api接口，下载的数据库文件
  ipip会定期更新地址信息，需要从网上下载
  需要安装第三方包datx
==============================
"""
import logging
import datx
import os

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


abs_path = os.getcwd()  # 运行程序的位置
dir_path = os.path.dirname(os.getcwd())  # 父目录
base_path = os.path.join(os.path.dirname(os.getcwd()), "address")  # 父目录组合


def ipip_get_add(ip):
    cc = datx.City(os.path.join(base_path, "ipdb.datx"))
    try:
        res = cc.find(ip)
    except ValueError as VE:
        print(VE)  # 这里可以做另外的处理，比如从纯真IP数据库里面再找
        res = ["unknown", "", "", ""]
    res = " ".join(res).strip()
    return res


def pure_get_add(ip):
    pass


if __name__ == '__main__':
    print(ipip_get_add("174.32.107.130"))



