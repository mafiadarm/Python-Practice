# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_14_2018  15:36
   File Name:      /GitHub/zhilianzhaopin
   Create From:     PyCharm
   Python version: 3.6.2
- - - - - - - - - - - - - - -
   Description:
   1 have a range
   2 guess num, if not hit, shrink range.
   3 hit the number, player win.
   4 hit the range of four in max side and min side, banker win.
==============================
"""

import random

__author__ = 'Loffew'


class CutNumber:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.n_range()

    def n_range(self):
        try:
            min_side = input("you want min_side to: ")
            max_side = input("you want max_side to: ")
            if 0 == len(min_side): min_side = 0
            if 0 == len(max_side): max_side = 100
            self.min = min(int(min_side), int(max_side))
            self.max = max(int(min_side), int(max_side))
        except ValueError:
            print("must be number!")
            return self.n_range()
        return self.min, self.max

    def random_num(self):
        return random.randint(self.min, self.max)

    @staticmethod
    def game_over():
        yn = input("game again? (Y or N): ")
        if yn.upper() == "Y": return True
        else: return False

    @staticmethod
    def hit_num(core, guess):
        if core == guess:
            print("number is", core, "banker drink")
            return False
        elif core < guess <= core + 4 or core - 4 <= guess < core:
            print("number is", core, "player drink")
            return False
        return True

    def num_return(self):
        core = self.random_num()
        cycle = True
        while cycle:
            print("now range is %s to %s" % (self.min, self.max))
            try:
                guess = int(input("guess the num: "))
            except ValueError:
                print("it is not num")
                continue

            if self.min < guess < core: self.min = guess
            elif core <= guess < self.max: self.max = guess
            else: print("is wrong number")
            cycle = self.hit_num(core, guess)

        return self.game_over()


def main():
    flag = True
    while flag:
        start = CutNumber()
        flag = start.num_return()


if __name__ == '__main__':
    main()
