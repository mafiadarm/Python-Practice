#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           06_29_2018  13:02
    File Name:      /GitHub/Daily
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""
import calendar
import time
import datetime

__author__ = 'Loffew'

a = "Sat Mar 28 22:24:24 2016"

cal = calendar.month(2016, 1)  # 打印日历

daily = {
    "datetime.date.today()": datetime.date.today(),
    "str(datetime.date.today())": str(datetime.date.today()),
    "datetime.datetime.now()": datetime.datetime.now(),
    "str(datetime.datetime.now())": str(datetime.datetime.now()),
    "time.time()": time.time(),
    "str(time.time())": str(time.time()),
    "time.localtime(time.time())": time.localtime(time.time()),
    'time.gmtime()': time.gmtime(),
    "time.asctime( time.localtime(time.time()))": time.asctime(time.localtime(time.time())),
    'time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,
    'time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())': time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()),
    'time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))': time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")),
    "time.ctime()": time.ctime(),
}

for k, v in daily.items():
    print(k, " "*(60-len(k)), v)