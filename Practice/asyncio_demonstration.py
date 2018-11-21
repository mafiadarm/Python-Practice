#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

__author__ = 'Loffew'
"""
==============================
    Date:           08_08_2018  16:57
    File Name:      /Practice/asyncio
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import asyncio
import random

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)


def tt():
    for i in range(3):
        yield i


def gen():
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = 'got: %s' % receive


g = gen()
print(g.send(None))
print(g.send('hello'))
print(g.send(123456))


# print(g.send('e'))


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


f = fab(10)
for i in f:
    print(i)


async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        await asyncio.sleep(1)


strlist = ["ss", "dd", "gg"]
intlist = [1, 2, 5, 6]
c1 = mygen(strlist)
c2 = mygen(intlist)

loop = asyncio.get_event_loop()
tasks = [c1, c2]
loop.run_until_complete(asyncio.wait(tasks))

print('All fib finished.')
loop.close()