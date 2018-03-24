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

data_info = {
    "server": "10.0.10.20",
    "user": "sa",
    "password": "UntXSO1X653Y",
    "database": "ROSUNDB",
}


conn = pymssql.connect(**data_info, charset="GBK")
cursor = conn.cursor()
# with pymssql.connect(server, user, password, database).cursor() as rr:
def close():
    cursor.close()
    conn.close()

def execution(sql):
    def order(*args, **kwargs):
        try:
            cursor.execute(sql(*args, **kwargs))
            conn.commit()
        except Exception as ex:
            conn.rollback()
            raise ex
        finally: close()
        return "Executed"
    return order

# 增（插入）
@execution
def insert(fields, *args):
    # fields = ("company", "creator", "create_date")
    # values = ("rosun", "ds", "20170101000011111")
    if len(fields) == len(args):
        return "INSERT INTO EMPLOYEE({}) VALUES ({})".format(fields, args)
# 删除
@execution
def delete(table_name, conditions):
    return "DELETE FROM {} WHERE {}".format(table_name, conditions)
# 更新
@execution
def update(table_name, content, condition):
    return "UPDATE {} SET {} WHERE {}".format(table_name, content, condition)


# 查询
def query(table_name, conditions=None):
    sql = 'SELECT * FROM {}'.format(table_name)
    if conditions:
        sql = sql + " WHERE {}".format(conditions)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()  # 使用fetchall()直接获取所有execute结果作为一个list：
        for i in result:
            print(i)
    except Exception as ex:
        print("here is error")
        pp_dbg(ex)
    finally:
        close()


sql_send = 'SELECT TOP 10 * FROM ROSUNDB.dbo.dl'
cursor.execute(sql_send)
for i in cursor.fetchall():
    print(i)
close()

# query("COPTG", "TG003=20130325")