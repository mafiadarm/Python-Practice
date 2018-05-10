#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           04_06_2018  9:14
  File Name:      /Project_useful/delete_files
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
from multiprocessing.dummy import Pool
import os
from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


def delete(file):
    os.remove(file)

folder = input("The folder path: ")
p = Pool()

for folder, _, files in os.walk(folder):
    for file in tqdm(files):
        path = os.path.join(folder, file)
        p.apply_async(delete, args=(path,))

p.close()
p.join()
