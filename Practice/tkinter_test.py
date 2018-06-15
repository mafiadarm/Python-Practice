#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           06_05_2018  20:33
  File Name:      /GitHub/tkinter_test
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
from tkinter import *
import random

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


def tz(width, height, colour):
    # print("This is a sentence!")
    x = random.randrange(width)
    y = random.randrange(height)
    x1 = y + random.randrange(height)
    y1 = x + random.randrange(width)
    canvas.create_rectangle(x, y, x1, y1, fill=colour, stipple="gray12", outline=colour, dash=10)

tk = Tk()  # 创建一个窗口
canvas = Canvas(tk, width=300, height=300)  # 画布
canvas.pack()
mycolour = ["red", "yellow", "blue", "grey", "cyan"]

for num in range(200):
    tz(200, 200, mycolour[num % 5])
# canvas.create_line(20, 10, 200, 100, fill="green", width=3)
# canvas.create_rectangle(50, 50, 100, 100, fill="red", stipple="gray12", dash=100)
# btn = Button(tk, text="Click to girl!", command=tz)
# canvas.create_polygon(100, 10, 130, 50, 80, 60, 110, 150, outline="red", fill="black")
# btn.pack()  # 显示界面

tk.mainloop()  # 循环允许窗口
