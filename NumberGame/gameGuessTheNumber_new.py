# -*- code:utf-8 -*-
"""
修改了排序，重新做了Guess The Number
在6-666的范围里面猜随机数

更新：每人分别有1次“过”“反”的技能
新增：按顺序猜
"""

from random import shuffle, randint


def playGame(player_list, secrit):
    genNum = 0
    while True:
        for turn in player_list:
            while genNum != 1:
                reGuess = errorDelay(player_list, turn, secrit)
                if reGuess == 1:
                    break
                else:
                    genNum = 0


def errorDelay(player_list, turn, secrit):
    try:
        guessNum = input("%s喊数字(6,666)：" % turn)
        if guessNum == "过":
            if "%s过" % turn not in skillList:
                skillList.append("%s过" % turn)
                return 1
            else:
                print("已经用过此技能了")
                return 0
        elif guessNum == "反":
            if "%s反" % turn not in skillList:
                skillList.append("%s反" % turn)
                reverseTurn(turn, player_list, secrit)
            else:
                print("已经用过此技能了")
                return 0
        elif int(guessNum.split(",")[0]) and int(guessNum.split(",")[1]):
            youRight = rightNum(turn, secrit, guessNum)
            if youRight == 0:
                return 0
            else:
                return 1
        else:
            print("请重新输入")
            return 0
    except IndexError:
        print("没有玩家")
        return 0
    except ValueError:
        print("值输入错误")
        return 0


def reverseTurn(player, playerlist, num):
    countNum = len(playerlist)
    tranList = list(range(countNum))
    caList = playerlist
    caList.reverse()
    indexNumber = caList.index(player)
    for ind in range(countNum):
        if indexNumber + 1 >= countNum:
            tranList[ind] = caList[indexNumber + 1 - countNum]
        else:
            tranList[ind] = caList[indexNumber + 1]
        indexNumber += 1
    return playGame(tranList, num)


def rightNum(turn, secrit, guessnum):
    guessList = list(range(int(guessnum.split(",")[0]), int(guessnum.split(",")[1]) + 1))
    if list(range(int(guessnum.split(",")[0]) >= int(guessnum.split(",")[1]))):
        print("不带这么玩儿的")
        return 0
    elif set(cacheList) - set(guessList) != set(cacheList):
        print("范围重复了")
        return 0
    elif int(guessnum.split(",")[0]) - cacheList[-1] != 1:
        print("喊跳了")
        return 0
    else:
        guess_RnR(turn, guessList, secrit)
        return 1


def guess_RnR(x, y, z):
    global cacheList
    if z in y:
        print("%s猜中了，答案是：%s" % (x, z))
        restart_exit()
    else:
        cacheList += y


def restart_exit():
    rex = input("退出请按“y”，继续游戏请按回车： ")
    if rex == "":
        gameStart()
    elif rex == "y":
        quit()
    else:
        restart_exit()


def gameStart():
    skillList.clear()
    peopleList, playNum = [], ""
    while playNum != "ok":
        playNum = input("玩家名字，输入\"ok\"结束： ")
        peopleList.append(playNum)
    peopleList.remove("ok")
    shuffle(peopleList)
    print("玩家顺序为：%s\n" % (' -> '.join(peopleList)))
    ranNum = randint(6, 666)
    playGame(peopleList, ranNum)


if __name__ == '__main__':
    skillList, cacheList, guessList = [], [1, 2, 3, 4, 5], []
    gameStart()
