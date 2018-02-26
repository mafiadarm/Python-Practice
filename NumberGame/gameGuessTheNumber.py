#-*- code:utf-8 -*-
#version 3.6

from random import shuffle,randint
peopleList,cacheList,skillList,guessList,playNum,guessNum,generalNum = [],[],[],[],"","",0

while playNum != "ok":
    playNum = input("玩家名字，输入\"ok\"结束： ")
    peopleList.append(playNum)

peopleList.remove("ok")  #或者del peopleList[-1]
shuffle(peopleList) #打乱顺序
lenNum = len(peopleList)
for a,b in enumerate(peopleList): #通知顺序
    print("->%s" %b,end="")
print()

ranNum = randint(6,666)

##while ranNum not in guessList:
while True:    
    for turn in peopleList:
        while generalNum != 1:
            try:
                guessNum = input("%s喊数字(6,666)："%turn)
                if guessNum == "过":
                    if "%s过"%turn not in skillList:
                        skillList.append("%s过"%turn)
                        generalNum = 1
                    else:
                        print("已经用过此技能了")
                elif guessNum == "乱":
                    if "%s乱"%turn not in skillList:
                        skillList.append("%s乱"%turn)
                        shuffle(peopleList)
                        print("现在的顺序是%s"%peopleList)
                        generalNum = 1
                    else:
                        print("已经用过此技能了")
                    
                elif type(list(range(int(guessNum.split(",")[0]),int(guessNum.split(",")[1])+1))) == list:
                    if list(range(int(guessNum.split(",")[0]) >= int(guessNum.split(",")[1]))):
                        print("不带这么玩儿的")
                    else:
                        guessList = list(range(int(guessNum.split(",")[0]),int(guessNum.split(",")[1])+1))
                        if set(guessList) - set(cacheList) == set(guessList):
                            if ranNum in guessList:
                                print("%s猜中了，答案是：%s"%(peopleList[0],ranNum))
                                generalNum = 1
                            else:
                                cacheList += guessList
                                generalNum = 1
                        else:
                            print("范围重复了")    
                else:
                    print(请重新输入)
            except IndexError:
                print("没有玩家")
            except ValueError:
                print("值输入错误")
