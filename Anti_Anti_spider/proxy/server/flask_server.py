#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_22_2018  14:59
  File Name:      /Anti_Anti_spider/flask_server
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  单独的一个应用程序，代理池启动后，本server单独启动
  从数据库读取数据，展示出来
==============================
"""
import random
import flask
from database.redis.Redis_save import RedisSet

app = flask.Flask(__name__)
pool = RedisSet().pool


@app.route("/")
def index():  # /?min=5&max=100
    args = flask.request.args  # 获取所有url里面的参数
    result = pool.zrangebyscore("working", args.get(min, 5, type=int), args.get(max, 10, type=int))
    proxy = random.choice(result)
    return proxy


def start_server():
    app.run(host="127.0.0.1", port=8888)


if __name__ == '__main__':
    start_server()
