# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_24_2018  11:39
   File Name:      /GitHub/skill_guessnum
   Create From:     PyCharm
   Python version: 3.6.2
- - - - - - - - - - - - - - - 
   Description:
   1 rule a range
   2 guess in order
   3 everyone have just two skills[pass and reverse] to use
   4 pass: do not do anything the turn
   5 reverse: reverse order and pass
==============================
"""

__author__ = 'Loffew'

import logging
from random import randint
from random import shuffle

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)


class GuessNumber:
    def __init__(self, min_range, max_range):
        print("This Game Range is {} to {}".format(min_range, max_range))
        self.min_range = min_range
        self.range = range(min_range, max_range)
        self.answer = randint(min_range, max_range)
        self.player_list = []
        self.skill_used = {"pass_reverse"}
        self.people_collection()
        self.people_turn()

    def get_answer(self, player, text="Mr.%s Please guess num or use skill: "):
        """
        get answer and filter.
        the answer must be (number or "pass" and "reverse").
        check if "pass" and "reverse" has been used
        """
        print("\nNow number is from %s\n" % self.min_range)
        answer = input(text % player)
        if answer == "pass" or answer == "reverse":
            if player + answer in self.skill_used:
                text = "YOU WERE USE THE SKILL, TAKE YOU MIND RUNNING! Mr.%s !"
                return self.get_answer(player, text)
            else:
                self.skill_used.add(player+answer)
                return answer

        try:
            tmp = [int(v) for v in answer.split(",")]
        except ValueError:
            text = "Mr.%s Please check! There must be (number or 'pass' and 'reverse') in 'en' status!"
            return self.get_answer(player, text)

        return max(tmp)

    def give_result(self):
        print()
        print("SO LUKY YOU GET IT!".center(30, "-"))
        print("THE NUMBER IS THE".center(30, "^"))
        print((" Oo^ %s ^oO " % self.answer).center(30, "*"))
        print("CONGRATULATIONS".center(30, "^"))

    def verify_answer(self, player):
        """
        skills have "pass, reverse".
        per skill have just one chance use to all turn of each one
        guess correct, you'll get point out!
        """
        answer = self.get_answer(player)
        if answer == "pass":
            self.around_and_around(player)
        elif answer == "reverse":
            self.player_list = self.player_list[::-1]
            self.people_turn()

        for num in range(self.min_range+1, answer+1):
            if num == self.answer:
                self.give_result()
                return True
        self.min_range = answer

    def around_and_around(self, player):
        """
        around and around the "self.player_list"
        update list when answer "pass"
        """
        self.player_list.remove(player)
        self.player_list.append(player)
        return self.people_turn()

    def people_turn(self):
        """
        people take turn guess the num.
        order in  "self.player_list"
        when turn ending, carry out self again
        if player answer "reverse" , it can be change list
        or ues cycle from itertools but not here
        """
        player = self.player_list[0]
        if self.verify_answer(player):
            return True
        self.around_and_around(player)

    def people_collection(self, shuffle_flag=True):
        """
        collection players to player_list.
        use "shuffle_flag" to choose shuffle or not shuffle.
        no repetitive name!
        """
        while True:
            players = input("PlayerName, Enter \"ok\" to START GAME: ")
            if players == "ok": break
            elif players is "": print("Give me some character")
            elif players not in self.player_list: self.player_list.append(players)
            else: print("Please do not input repetitive name!")

        if len(self.player_list) is 0:
            print("There is nobody")
            self.people_collection()
        if shuffle_flag:
            shuffle(self.player_list)


def main():
    while True:
        guess_range = input("What Range Do You Want? Please input min and max (default is 6 to 666):")
        if len(guess_range) is 0:
            xx = (6, 666)
            break
        elif len(guess_range.split(",")) > 1:
            try:
                xx = [int(i) for i in guess_range.split(",")]
                break
            except ValueError: print("IS NOT All of NUMBER!\n")
        else: print("IS NOT NUMBER!or GIVE ME TWO NUMBER\n")

    GuessNumber(min(xx), max(xx))


if __name__ == '__main__':
    while True:
        main()
        again = input("\nDo you want again? Enter 'N' to exit: ")
        again.upper()
        if again is "N":
            raise SystemExit
