# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_23_2018  9:29
   File Name:      /GitHub/updateProduce
   Creat From:     PyCharm
- - - - - - - - - - - - - - -
   Description:   玩家选择一个拳，有三个选择 石头、剪刀、布
                  机器随机出一个数，1,2,3 对应石头、剪刀、布
==============================
"""

__author__ = 'Loffew'

from random import randint


def pp_result(items_dict, lwidth, rwidth):
    print(("总局数:%s" % count_round).center(lwidth + rwidth, "-"))
    for k, v in items_dict.items():
        print(k.ljust(lwidth, ".") + str(v).rjust(rwidth))


count_round = 0
count_result = {"p": 0, "s": 0, "f": 0}

while 1 > 0:
    s, r = randint(1, 3), randint(1, 3)  # 自动测试
    # r = int(input("1.石头 2.剪刀 3.布 选择一个（输入1-3）："))  # 手动玩
    rule = {
        (1, 1): None, (1, 2): True, (1, 3): False,
        (2, 1): False, (2, 2): None, (2, 3): True,
        (3, 1): True, (3, 2): False, (3, 3): None
    }
    result = (r, s)

    if rule[result] is None:
        print("\n平局\n")
        count_result["p"] += 1
    elif rule[result]:
        print("\n赢了\n")
        count_result["s"] += 1
    else:
        print("\n输了\n")
        count_result["f"] += 1

    count_round += 1

    items = {
        "胜率": "%.6f" % (count_result["s"] / count_round),
        "败率": "%.6f" % (count_result["f"] / count_round),
        "平局": "%.6f" % (count_result["p"] / count_round)
    }

    pp_result(items, 10, 10)
