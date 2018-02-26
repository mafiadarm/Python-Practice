#version 3.6
#获得菲波拉契数 每按一次，出2组10行，可以终止
def fib_Creat():
    from produce import pro
    a = int(input("How many do you want: "))
    b = pro(a)
 
    try:
        s = 0
        while s < a :
            next(b)
            print("---------------cut off-----------------")
            s += 1
            if s%2 == 0:
                dd = input("Do you go on? k_stop： ")
                if dd == "k":
                    raise TypeError
                else:
                    pass
 
    except StopIteration:
        print("Over")
    except TypeError:
        print("Stop")
