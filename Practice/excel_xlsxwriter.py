# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_21_2018  13:44
   File Name:      /GitHub/excel_xlsxwriter
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
==============================
"""
import logging
import xlsxwriter

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def printdbg(*args):
    return logging.debug(*args)


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet("information")

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 19)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# 设置格式
ff = workbook.add_format()
ff.set_align('justify')
ff.set_align('center')
ff.set_align('vjustify')
ff.set_align('vcenter')
ff.set_text_wrap()

# Write some simple text.
worksheet.write('A1', 'Hello', ff)

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.  图片是可以设置大小的
# worksheet.insert_image('B5', 'logo.png')

workbook.close()
