#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_25_2018  13:26
    File Name:      /proxy_pool/Redis_save
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    用无序的redis，直接去重就行了，减少中间运算的复杂程度

    新ip加入方式：
        保存以"ip:port" 的格式保存
        key: await 装载所有爬取到的值格式为 1 "0.0.0.0:0000"
    验证后保存到可使用的key里面
    可使用保存方式：
        保存以"ip:port:response"的格式保存
        key: working 装载所有爬取到的值格式为 100 "0.0.0.0:0000:0"
    循环检查方式：
        计算总共有多少个值，遍历范围，一段一段的检查
        如果能使用，则原值分数-100，新值添加到里面
        如果不能用，则原值分数-1
        最后删除 -100 到 -50 的值

==============================
"""

from database.redis.redis_connect import RedisConnect


class RedisSet(RedisConnect):
    """
    使用有序集合进行管理，并对分数进行管理
    """
    def __init__(self, host=None, port=None, db=None):
        super().__init__(host=host, port=port, db=db)
        self.pipe = self.pipeline()
        self.pool = self.connect_pool()

    """
    Set集合就是不允许重复的列表
    可以直接用初始化里面的连接实例直接进行操作，或者查询对应方法使用私有方法进行操作
    """

    def add_to(self, a_type, key_name, *args, **kwargs):
        if a_type == "zadd": self.pool.zadd(key_name, *args, **kwargs)  # 有序 !!大坑，值和分数要反过来写

    def sdelete(self, d_type, key_name, *args):
        if d_type == "delete": self.pool.zremrangebyscore(key_name, *args)  # 根据分数范围删除值
        if d_type == "zrem": self.pool.zrem(key_name, *args)  # 根据分数范围删除值

    def supdate(self, u_type, key_name, *args):
        if u_type == "zincrby": self.pool.zincrby(key_name, *args)  # name, value, amount=±1 修改值的分数

    def squery(self, q_type, key_name, value=None, start=None, end=None):
        if q_type == "zrange": self.pool.zrange(key_name, start, end)  # 通过索引范围获取值
        if q_type == "zrangebyscore": self.pool.zrangebyscore(key_name, start, end)  # 通过分值范围获取值
        if q_type == "zcard": self.pool.zcard(key_name)  # 获取key里面包含值的个数，遍历取数的时候用
        if q_type == "zscore": self.pool.zscore(key_name, value)  # 获取值的分数


