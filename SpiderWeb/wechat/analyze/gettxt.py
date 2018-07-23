#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_26_2018  15:38
    File Name:      /wechat/gettxt
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import re

import os
from analyze.run_sqlite import WeChat
from analyze.PATH_SETTING import *

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def disponse(wechat):
    """
    把words.txt里面的数据写到数据库
    :return:
    """
    regx = re.compile(r"message:(.*?)----------")
    gethan = re.compile(r"Group: (.*?)>.*?Member: (.*?)>.*?(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?\t(.*?)<\|(.*?)\|>")
    hanzi = re.compile(r"\w+")

    if not os.path.exists(WORDS):
        return

    with open(f"{WORDS}", "r", encoding="utf-8") as rr:
        aaa = rr.readlines()
        bbb = "".join(aaa).replace("\n", "")

    result = regx.findall(bbb)

    for i in result:  # '<Group: 🐷小猪佩奇小卖部🐷>\t<Member: 这个群里，我是最帅的>\t2018-04-25 16:54:30.047209\tText<|[捂脸]|>'
        gett = gethan.findall(i)

        if gett:
            j = gett[0]
            chat = "_".join(hanzi.findall(j[0]))
            member = "_".join(hanzi.findall(j[1]))
            dd = j[2]
            tt = j[3]
            text = "_".join(hanzi.findall(j[4]))

            we.checkIn(chat, member, text, tt, dd)

    we.conn.commit()
    os.remove(f"{WORDS}")


if __name__ == '__main__':
    we = WeChat()
    disponse(we)
    we.finish()

