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
==============================
"""
import random
import flask
from proxy_pool.database.Mongo_Save import Mongo_Helper

app = flask.Flask(__name__)


@app.route("/")
def index():
    res_dict = flask.request.args  # 获取所有url里面的参数
    json_result = Mongo_Helper().select(count=int(res_dict.get("count", 1)))
    proxy = random.choice(json_result)
    return f"{proxy[0]}:{proxy[1]}"


def start_server():
    app.run(host="127.0.0.1", port=8888)


if __name__ == '__main__':
    start_server()
