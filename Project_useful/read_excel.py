#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_26_2018  17:59
   File Name:      /GitHub/read_excel
   Creat From:     PyCharm
   Python version: 3.6.2  
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

import logging
import xlrd

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def open_excel():
    # 打开文件
    data = xlrd.open_workbook("C:/Users/loffew/Desktop/133.xlsx")

    # 获取一个工作表
    table = data.sheets()[0]             #通过索引顺序获取
    # table = data.sheet_by_index(0)       #通过索引顺序获取
    # table = data.sheet_by_name(u'Sheet') #通过名称获取

    # 获取行数和列数
    nrows = table.nrows
    ncols = table.ncols

    # 获取整行和整列的值（数组）
    for i in range(nrows):
        pp_dbg(table.row_values(i))
    for i in range(ncols):
        pp_dbg(table.col_values(i))

    # 单元格
    # cell_A1 = table.cell(0, 0).value
    # cell_C4 = table.cell(2, 3).value

    # 使用行列索引
    # cell_A1 = table.row(0)[0].value
    # cell_A2 = table.col(1)[0].value


if __name__ == '__main__':
    import win32com.client

    xlApp = win32com.client.DispatchEx("Excel.Application")
    xlApp.Visible = False  # 打开excel时是否可见
    print("Excel library version:", xlApp.Version)
    xlwb = xlApp.Workbooks.Open(Filename="C:/Users/loffew/Desktop/133.xlsx", UpdateLinks=2, ReadOnly=False, Format=None, Password='HQ1030',
                                WriteResPassword='12345')