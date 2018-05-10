#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_11_2018  16:27
    File Name:      /Collection/qq_chat_robot
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    https://github.com/pandolia/qqbot

==============================
"""

import random
from qqbot import QQBotSlot as qqbotslot, RunBot
from run_sqlite import *

__author__ = 'Loffew'


@qqbotslot
def onQQMessage(bot, contact, member, content):
    thme = datetime.datetime.now()
    hour = thme.hour

    if content == "宝宝" and member and contact.name == "Empire😘😘":
        socker = random.randint(100, 666)

        if socker == 666:
            bot.SendTo(contact, "@" + member.name + "\n*-❤*-心情美丽-*❤-*\n爱你爱你$^%s^$么么哒\n想和宝宝睡午觉么\nO(∩_∩)O" % (socker, ))

        obj = qq.query(member.name)

        if qq.flag == 1:
            bot.SendTo(contact, "@" + member.name + "\n知道啦知道啦\n\n╭(╯^╰)╮\n\n今天已经打过招呼啦！")
        else:
            bot.SendTo(contact, "@" + member.name + "\n哦哟哟~您来啦~啦啦啦\n给你一个♥(ˆ◡ˆԅ)\n增加了 -* %d *-爱您值哦~\n\n宝宝有 -* %d *- 爱您了呢~！" % (socker, obj[0][1]+socker))

        qq.checkIn(member.name, socker)

    # if "@ME" in content:
    #     bot.SendTo(contact, "@" + member.name + "\n嘤嘤嘤，来啦来啦，我家主人不在加呢~\n宝宝继续睡觉觉啦\n\n\t么么哒~❤")

    if content == "[@ME]" + "  亲亲":
        if 8 < hour < 12 or 13 < hour < 17 or 19 < hour < 22:
            bot.SendTo(contact, "mua~mua~mua~mua~")
            qq.checkIn(member.name, random.randint(5, 10))
    elif content == "[@ME]" + "  亲你哟":
        if 8 < hour < 12 or 13 < hour < 17 or 19 < hour < 22:
            bot.SendTo(contact, "mua~mua~mua~mua~")
            qq.checkIn(member.name, random.randint(8, 10))
    elif content == "[@ME]" + "  爱你哟":
        if 8 < hour < 12 or 13 < hour < 17 or 19 < hour < 22:
            bot.SendTo(contact, "❤❤❤❤❤\n ❤❤❤❤\n   ❤❤❤\n     ❤❤\n       ❤")
            qq.checkIn(member.name, random.randint(10, 20))
    elif content == "[@ME]" + "  吃饭啦":
        if 8 <= hour < 9 or 12 <= hour <= 13 or 18 <= hour <= 19:
            bot.SendTo(contact, "宝宝正咋吃饭呢！❤\n\n喂您一口~啊~~")
            qq.checkIn(member.name, random.randint(30, 50))
    elif content == "[@ME]" + "  该睡觉啦":
        if hour >= 22:
            bot.SendTo(contact, "呼~呼~z~z~Z~Z~Z~")
            qq.checkIn(member.name, random.randint(30, 50))
    elif "rua" in content:
        if hour < 22:
            bot.SendTo(contact, "@" + member.name + "好长的舌头")
    elif "豆豆" in content:
        if hour < 22:
            bot.SendTo(contact, "吃饭睡觉打^豆o豆^~")
    elif content == "签到" :
        bot.SendTo(contact, "@" + "ʚ墨墨ɞ" + "快来啊~有人签到啦")
    elif content == "[@ME]" + "  宝宝你有多爱我":
        obj = qq.query(member.name)
        bot.SendTo(contact, "@" + member.name + "我有爱你有 %s 米深" % obj[0][1])
    elif content == "[@ME]" + "  宝宝":
        bot.SendTo(contact, "如果喜欢宝宝的话，可以\n@我\n亲亲\n亲你哟\n吃饭啦\n该睡觉啦\n\n想知道我有多爱你么？\n@我 问我多爱你❤")


if __name__ == '__main__':
    qq = SqliteQQ()
    RunBot()
