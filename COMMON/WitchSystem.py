# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_24_2018  21:54
   File Name:      /GitHub/WitchSystem
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
   判断操作系统类型
==============================
"""
import logging
import platform

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def printdbg(*args):
    return logging.debug(*args)


def ToPlatform():
    print("Get Operation System".center(30, "-"))

    print(platform.architecture())
    # Windows will be : (32bit, WindowsPE)
    # Linux will be : (32bit, ELF)

    print(platform.platform())
    # Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    # Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final

    print(platform.system())
    # Windows will be : Windows
    # Linux will be : Linux

    print("Python Version".center(30, "-"))
    print(platform.python_version())
    # Windows and Linux will be : 3.1.1 or 3.1.3


def UsePlatform():
    """
    Windows | Linux | Other System
    """
    return platform.system()

print(ToPlatform())