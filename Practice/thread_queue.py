#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

__author__ = 'Loffew'
"""
==============================
    Date:           08_08_2018  16:24
    File Name:      /Practice/thread_queue
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
from multiprocessing import Process, Manager

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)


def give_task(give_q):
    while 1:
        give_q.put("give!")


def get_task(get_q):
    while 1:
        print(get_q.get())


if __name__ == '__main__':
    queue = Manager().Queue()
    #
    give_process = Process(target=give_task, args=(queue, ))
    get_process = Process(target=get_task, args=(queue, ))

    give_process.start()
    get_process.start()

    give_process.join()
    get_process.join()