#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           08_31_2018  10:08
  File Name:      /Python-Practice/check_version
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - -
  Description:
==============================
"""
# 检查Python版本
from sys import version_info


def checkversion():
    if version_info.major != 3:
        raise Exception('请使用Python 3 来完成此项目')
