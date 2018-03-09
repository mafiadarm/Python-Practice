#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
   Date:           03_05_2018  9:46
   File Name:      /GitHub/SqlServerUse
   Creat From:     PyCharm
   Python version: 3.6.2  
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

import logging
import pymssql

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

server = "10.0.10.20"
user = "sa"
password = "UntXSO1X653Y"
database = "STUDY"

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()
# with pymssql.connect(server, user, password, database).cursor() as rr:
def close():
    cursor.close()
    conn.close()

def execution(sql):
    def order(*args, **kwargs):
        cursor.execute(sql)
        conn.commit()
        close()
        return sql(*args, **kwargs), "are executed"
    return order

# 增（插入）
@execution
def insert(fields, values):
    # fields = ("company", "creator", "create_date")
    # values = ("rosun", "ds", "20170101000011111")
    if len(fields) == len(values):
        return "INSERT INTO EMPLOYEE({}) VALUES ({})".format(fields, values)
# 删除
@execution
def delete(table_name, conditions):
    return "DELETE FROM {} WHERE {}".format(table_name, conditions)
# 更新
@execution
def update(table_name, content, condition):
    return "UPDATE {} SET {} WHERE {}".format(table_name, content, condition)
# 查询
def query(table_name):
    try:
        cursor.execute('SELECT * FROM {}'.format(table_name))
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception:
        print("here is error")
    finally:
        close()