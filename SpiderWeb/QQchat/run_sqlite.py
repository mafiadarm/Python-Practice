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
import datetime

__author__ = 'Loffew'

# logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


class SqliteQQ:
    def __init__(self):
        self.conn = sqlite3.connect('checkin.db')
        self.corr = self.conn.cursor()
        self.corr.execute(
            """CREATE TABLE IF NOT EXISTS Empire (username nvarchar(50), socker int nvarchar(50), changedate date);"""
        )
        self.flag = 0

    def querySocker(self, username):
        self.flag = 0
        self.corr.execute("SELECT * FROM Empire WHERE username='{}';".format(username))
        obj = self.corr.fetchall()

        if obj and obj[0][2] == str(datetime.date.today()):
            self.flag = 1

        return obj  # [("","",""),("","","")]

    def checkIn(self, username, socker):

        obj = self.querySocker(username)

        if not obj:
            self.corr.execute("INSERT OR REPLACE INTO Empire VALUES ('{}', 20, date('now'));".format(username))
        else:
            self.corr.execute("UPDATE Empire SET socker = socker + {}, changedate = date('now') WHERE username='{}';".format(socker, username))

        self.conn.commit()

    def finish(self):
        self.corr.close()
        self.conn.close()


class Jokes:
    def __init__(self):
        self.conn = sqlite3.connect('joker.db')
        self.corr = self.conn.cursor()

    def queryJoke(self):
        self.corr.execute("SELECT content FROM JOKES ORDER BY RANDOM() limit 1")
        joke = self.corr.fetchall()
        return joke[0][0]

    def finish(self):
        self.corr.close()
        self.conn.close()
        

if __name__ == '__main__':
    qq = SqliteQQ()
    qq.checkIn("om", 20)
    qq.finish()
