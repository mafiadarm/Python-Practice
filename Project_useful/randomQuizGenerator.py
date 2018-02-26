# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_17_2018  16:08
   File Name:      /GitHub/randomQuizGenerator
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:    关于国家和首府的题
   1 创建 N 份不同的试卷
   2 为每份试卷创建50多重选择题
   3 为每个题提供1个正确答案和3个随机错误答案
   4 将试卷写到文本中
==============================
"""
__author__ = 'Loffew'

import random
#  建一个装有所有国家和首府的字典
with open("capitals.txt", "r") as rr:
    ss = rr.readlines()

capitals = {}
# 处理字典
for i in range(len(ss)):
    cha = ss[i].replace("\n", "")
    chb = cha.split("\t")
    capitals[chb[0]] = chb[1]

# 创建试卷和答案的文件
for quizNum in range(1):  # 想要多少试卷就在这里填入多少试卷
    quizFile = open("capitals_quiz%s.txt" % (quizNum + 1), "a+")
    answerKeyFile = open("capitals_answer%s.txt" % (quizNum + 1), "a+")
    # 创造填写个人信息的位置
    quizFile.write("Name:\nDate:\nPeriod:\n\n")
    quizFile.write((" " * 20) + "State Capitals Quiz (Form %s)" % (quizNum + 1))
    quizFile.write("\n\n")

    # 打乱列表顺序
    states = list(capitals.keys())
    random.shuffle(states)

    # 制造 题和可选答案
    for questionsNum in range(50):
        correctAnswer = capitals[states[questionsNum]]  # 获取正确答案
        wrongAnswers = list(capitals.values())  # 赋值所有答案到wrongAnswers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # 从wrongAnswers删除正确答案
        wrongAnswers = random.sample(wrongAnswers, 3)  # 随机选3个
        answerOptions = wrongAnswers + [correctAnswer]  # 拼接答案
        random.shuffle(answerOptions)  # 再次打乱顺序

        # 题目
        quizFile.write("%s. %s 的首都是:\n\n" % (questionsNum + 1, states[questionsNum]))

        # 选项
        for i in range(4):
            quizFile.write(" %s. %s\n" % ("ABCD"[i], answerOptions[i]))
            quizFile.write("\n")

        # 把答案写到答案文件夹
        answerKeyFile.write("%s. %s\n" % (questionsNum + 1, "ABCD"[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()

