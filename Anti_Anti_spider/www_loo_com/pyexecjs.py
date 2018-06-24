#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           06_18_2018  21:07
  File Name:      /GitHub/pyexecjs
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  pip install pyexecjs
  相对于python2 的PyV8来使用，功能没那么强大，但是一样好用
  测试对象为www.luoo.net，设置dom事件触发break on
  在检查元素，查询audio标签，播放MP3是必须要用这个固定标签
  在路径上用break on --> attribute modifications 当此处有变化的时候会跳到js代码
  从右边call stack去一步一步的找数据来源，每一步都看看js值的变化
  找到自己想要的值，再看这个值从什么方法得来的（可以找找最后产生这个方法的类赋值的地方）
  这个类传了那些参数进去，找到这些参数，看看这次参数怎么产生的，点F11进去看逻辑
  如果进去再出来，还在同一个位置，就必须再进去看看，因为里面肯定有东西变化了

  用找到的js逻辑，重新构建一个js文件，只取产生作用的函数方法，以及函数里面的参数值，没有的就直接定义
==============================
"""

__author__ = 'Loffew'

import execjs
from luo_pl import PL


def execjs_demo():
    # 执行js代码
    e = execjs.eval("a = new Array(1,2,3)")
    print(e)

    # 加载js代码，传参
    ctx = execjs.compile("""
        function add(x, y){
            return x+y
        };
    """)
    print(ctx.call("add", 1, 2))


def call_js():
    with open("add.js", "r", encoding="utf-8") as rr:
        js = rr.read()

    aes = "b6ce159334e155d8"
    ctx = execjs.compile(js)  # 加载js环境到python
    code = ("N", PL, aes)
    print(ctx.call(*code))  # 在环境里面执行js语句

if __name__ == "__main__":
    # execjs_demo()
    call_js()