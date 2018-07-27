#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_16_2018  23:27
  File Name:      /Anti_Anti_spider/Mongo_save
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
import pymongo

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


class Mongo_Helper:
    def __init__(self):
        self.client = pymongo.MongoClient()  # 本地数据库可以不写地址和端口
        self.db = self.client.proxy
        self.proxies = self.db.proxies

    def insert(self, proxy):
        """
        insert data
        :param proxy:
        :return:
        """
        if proxy:
            proxy = dict(ip=proxy["ip"], port=proxy["prot"], addr=proxy["addr"], speed=proxy["speed"], score=5)
        self.proxies.insert(proxy)

    def delete(self, conditions):
        """
        :param conditions:
        :return:
        """
        if conditions:
            self.proxies.remove(conditions)
            print("delete {} complete".format(conditions))

    def update(self, conditions, value):
        """
        :param conditions:
        :param value:
        :return:
        """
        if conditions and value:
            self.proxies.update(conditions, {"$set": value})

    def select(self, count=0):
        count = int(count) if count else 0
        items = self.proxies.find({}, limit=count).sort("score", pymongo.DESCENDING)
        results = []
        for item in items:
            result = [item["ip"], item["port"], item["score"]]
            results.append(result)
        return results


if __name__ == '__main__':
    # Mongo_Helper().insert({"ip": "127.0.0.1", "port": 8080, "addr": "湖南 长沙"})
    m = Mongo_Helper()
    # m.update({"ip": "127.0.0.1"}, {"addr": "北京"})
    # a = m.select(1)
    # print(a)
    # m.delete({"ip": "127.0.0.1"})
