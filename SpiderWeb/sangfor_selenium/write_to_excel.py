#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_04_2018  12:15
    File Name:      /GitHub/write_to_excel
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""
import xlsxwriter


def into_excel(name, table):
    # 写入excel
    workbook = xlsxwriter.Workbook(f'{name}.xlsx')
    worksheet = workbook.add_worksheet("information")

    for i, data in enumerate(table):
        for j, value in enumerate(data):
            print(i, j, value)
            worksheet.write(i, j, value)

    workbook.close()
