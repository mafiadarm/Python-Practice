#version 3.6
#以if和while为主的小游戏

import random

print('''

---@---扫地小游戏---@---
1、摇骰子决定猜数字的顺序
2、封顶数为：人数总和*6
3、答案为人数总和乘以6以内的数字
4、每人至少猜1个数字，最多猜3个数字
5、不能重复猜数字
6、每人有一次喊反转（顺序）的权利和一次喊过（自己）的权利
7、猜中的去扫地
---@---扫地小游戏---@---

''')


while True:
    p1 = input("\n-----$游戏开始&----\n\n总共多少人:")
    if p1.isdigit():
        p1 = int(p1)
        wx = p1 * 6
        n = random.randint(0,wx)
        a = 0
        li = []
        while a != n:
            a = input("猜猜是个啥，≤%s的数字："%wx)
            if a.isdigit():
                a = int(a)
                if a in li:
                    print("\n已经猜过了\n")
                else:
                    if a > wx:
                        print("\n谁给你单子猜这么大数字的？\n")
                    else:
                        if a == n:
                            print('''

        --------@-----@-------
           猜对了，去扫地吧
        --------@-----@-------

                                ''')
                        elif a != n: 
                            print("\n再猜\n")
                            li.append(a)                        
            else:
                print("\n喊你输数字\n")
    else:
        print("\n请输入数字\n")    
print("谜底是：%s"%n)

