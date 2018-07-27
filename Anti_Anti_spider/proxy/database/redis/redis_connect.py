#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_25_2018  10:34
    File Name:      /proxy_pool/redis_connect
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    提前安装redis
    pip install redis
==============================
"""

import redis
from database.ip_verify import ip_auth

__author__ = 'Loffew'


class RedisConnect:
    def __init__(self, host=None, port=None, db=None):
        self.host = host if host and ip_auth(host) else "127.0.0.1"
        self.port = port if port and issubclass(port, (int,)) else 6379
        self.db = db if db and issubclass(port, (int,)) else 0

    def connect(self):
        """
            redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，
            StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，
            Redis是StrictRedis的子类

        redis 连接方式
        :return: redis实例  此实例默认为本机第一个数据库
        """
        rr = redis.Redis(host=self.host, port=self.port, db=self.db)
        return rr

    def connect_pool(self):
        """
            redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
            默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，
            这样就可以实现多个Redis实例共享一个连接池。

        :return:此实例返回一个连接池实例
        """
        pp = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)
        rr = redis.Redis(connection_pool=pp)
        return rr

    def pipeline(self):
        """
            redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
            如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
            并且默认情况下一次pipline 是原子性操作。

            类似于mysql的事务提交
            获取实例后，做服务器命令，然后直接 [pipeline].execute()
        :return:
        """
        rr = self.connect_pool()
        pipe = rr.pipeline(transaction=True)
        return pipe


class Publish(RedisConnect):
    """
    首先定义一个RedisHelper类，连接Redis，定义频道为monitor，定义发布(publish)及订阅(subscribe)方法。
    """

    def __init__(self, host=None, port=None, db=None, channel_name=None):
        super(Publish).__init__(host=host, port=port, db=db)
        if not channel_name or not issubclass(channel_name, (str,)):
            channel_name = "monitor"
        self.__conn = self.connect_pool()
        self.channel = channel_name

    def publish(self, message=None):
        """
        定义发布方法
        :param message:
        :return:
        """
        self.__conn.publish(self.channel, message)
        return True

    def subscribe(self):
        """
        定义订阅方法
        :return:
        """
        sub = self.__conn.pubsub()
        sub.subscribe(self.channel)
        sub.parse_response()
        return sub


if __name__ == '__main__':
    # 发布
    Publish().publish("发布信息")

    # 订阅
    sub_get = Publish().subscribe()
    while 1:
        get_message = sub_get.parse_response()
        print(get_message)
