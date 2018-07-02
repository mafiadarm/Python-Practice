#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_03_2018  0:14
  File Name:      /GitHub/CaesarEncrypt
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  最初用于虾米的mp3下载
  json?_ksTS=1530553775819_389&callback=jsonp390
  返回的response里面有个location的keys，取出value值
==============================
"""
from urllib.parse import unquote

__author__ = 'Loffew'


def decrypt(text):
    chief_num = int(text[:1])
    text = text[1:]
    column = len(text) // chief_num  # 求出每行有多少个字符
    ends = len(text) % chief_num  # 求余数

    if ends:
        cut_list = [column+1 if i < ends else column for i in range(chief_num)]
    else:
        cut_list = [column] * chief_num

    str_list = []  # 把text切成一段一段的
    old_x = 0
    for x in cut_list:
        str_list.append(text[old_x:old_x+x])
        old_x += x
    print(str_list)

    url = ""
    for i in range(len(str_list[0])):  # 列数 以第一串字符串长度为准
        for j in range(chief_num):  # 行数 从开始就固定的
            print(j, i)
            url += str_list[j][i]  # 每行轮流取头
            print(url, len(url), len(text))
            if len(url) == len(text):
                return url


if __name__ == '__main__':
    ss = "7h%1.3F3E59%.t2.n3315E35mtFxe83%%16Epp%it27227563%2a%1%F56383Fm2%5%28_7AfiF2E5%966"
    print(unquote(decrypt(ss)).replace("^", "0"))



