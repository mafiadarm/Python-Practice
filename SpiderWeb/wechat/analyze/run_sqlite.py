#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_11_2018  22:17
    File Name:      /Collection/run_sqlite
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import sqlite3
from .PATH_SETTING import DATABASE

__author__ = 'Loffew'

# logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


class WeChat:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.corr = self.conn.cursor()
        self.corr.execute(
            """CREATE TABLE IF NOT EXISTS wechat (groupname text, username text, content text, gettype text, getdate datetime);"""
        )

    def checkIn(self, chat, member, text, tt, dd):
        self.corr.execute("INSERT INTO wechat VALUES ('{}', '{}', '{}', '{}', '{}');".format(chat, member, text, tt, dd))

    def query(self, sql):
        return self.corr.execute(sql).fetchall()

    def finish(self):
        self.corr.close()
        self.conn.close()


if __name__ == '__main__':
    qq = WeChat()
    qq.checkIn('', '', '_180426-124555.png', 'Picture', '2018-04-26 12:45:55')
    qq.conn.commit()
    qq.finish()
