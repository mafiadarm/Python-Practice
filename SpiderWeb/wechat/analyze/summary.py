#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_27_2018  23:51
    File Name:      /wechat/summary
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging

import os
import re
from collections import Counter
from multiprocessing.dummy import Pool

from .run_sqlite import WeChat
from .cloudwords import make_picture
from .PATH_SETTING import *
# from analyze.gettxt import disponse

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def multimedia():
    count_user = {}
    regx = re.compile(r"(.*?)_(.*?)_(\d{2})(\d{2})(\d{2})-\d+\.(.*?)$")
    # 拿出所有files
    for _, _, files in os.walk(f"{MULTIMEDIA}"):
        for file in files:
            # print(file)
            # print(regx.findall(file))
            # 拆分名字
            if regx.findall(file):
                group, name, d1, d2, d3, suffix = regx.findall(file)[0]
            else:
                continue
            # 获取指定群的信息
            if group == GROUPNAME and STARTDAY <= f"20{d1}-{d2}-{d3}" <= ENDDAY:
                # 名字：[后缀]
                if name in count_user:
                    count_user[name].append(suffix)
                else:
                    count_user[name] = [suffix]
    # print(count_user)
    for name, suffixes in count_user.items():
        print(name, "-"*20)
        for tt, con in Counter(suffixes).items():
            if tt == "png":
                print(f"--> {con} 张图片")
            if tt == "gif":
                print(f"--> {con} 个表情")
            if tt == "mp3":
                print(f"--> {con} 条语音")
        print()


def get_people():
    sql = "SELECT DISTINCT username, content, getdate FROM wechat WHERE groupname LIKE'{}' and gettype='Text' and getdate < '{} 00:00:00' and getdate>'{} 00:00:00';".format(GROUPNAME, ENDDAY, STARTDAY)
    result = we.query(sql)  # [(1093,)]
    # print(result)
    """
    用户名：发言次数
    用户名：发图次数 从文件夹里面搜索
    词云分析
    个人词云分析
    """
    user_count = {}
    regx = re.compile(r"\[.*?\]")
    for user, words, _ in result:

        face = set(regx.findall(words))
        for ace in face:
            words = words.replace(ace, "_")  # 去掉[]里面的表情

        if user in user_count:
            user_count[user].append(words)
        else:
            user_count[user] = [words]

    # print(user_count)

    all_words = []
    for user, words in user_count.items():
        # print(user, " 发言：", len(words), " 句话")
        # print(words)
        p.apply_async(make_picture, args=(words, user,))
        all_words.extend(words)

    # print(all_words)
    make_picture(all_words, GROUPNAME)


def disponse():
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
    p = Pool()
    we = WeChat()
    disponse()
    get_people()
    we.finish()
    p.close()
    p.join()
    multimedia()
