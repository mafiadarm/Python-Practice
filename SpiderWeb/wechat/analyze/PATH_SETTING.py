#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_28_2018  14:26
    File Name:      /wechat/PATH_SETTING
    Creat From:     PyCharm
    Python version: 3.6.2
- - - - - - - - - - - - - - -
    Description:
==============================
"""
import datetime


def TODAY(*arg):
    if not arg:
        return datetime.date.today()
    else:
        return datetime.date(*arg)


DATE = (2018, 4, 27)  # (2018, 4, 27)
BACKGROUND = "./img_face.jpg"
MULTIMEDIA = "wechat_photo/"
CLOUDWORDS = "./words_png/"
WORDS = "./words.txt"
GROUPNAME = "小猪佩奇小卖部"

STARTDAY = str(TODAY(*DATE))  # "2017-01-01"
DAYRANGE = 100  # 间隔天数
ENDDAY = str(TODAY(*DATE) + datetime.timedelta(days=DAYRANGE))

DATABASE = "checkin.db"


