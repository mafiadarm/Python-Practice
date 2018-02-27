#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_26_2018  16:02
   File Name:      /GitHub/GUI
   Creat From:     PyCharm
   Python version: 3.6.2  
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

import logging
from tkinter import *

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


root = Tk(className="转啊转啊转啊转")
root.geometry('400x400+300+100')  # 界面（宽x长+x轴+y轴）


def click():  # 定义按钮
    print('HAHA')  # 每按一次，运行一次


Button(root, text='push', command=click, bg='red').pack(fill=X, expand=1)  # （权限，按钮上的文字，控制命令，按钮颜色）
# root.mainloop()  # 定义回环

li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()  # 进入消息循环
