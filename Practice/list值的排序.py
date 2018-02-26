#-*- code:utf-8 -*-
'''
在循环中修改list值的排序
'''

li = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10"]


def yy(lis):
    while True:
        for ind,val in enumerate(lis):
            a = input("(%s)%s____: "%(ind,val))
            if a == "ok":
                return xx(val,lis)
def xx(x,y):
    ls = list(range(len(li)))
    ln = y
    ln.reverse()
    b = ln.index(x)
    for ind in range(len(ln)):
        if b+1 >= len(ln):
            ls[ind] = ln[b+1-len(ln)]
            print(ln,b+1-len(ln),ln[b+1-len(ln)])
        else:
            ls[ind] = ln[b+1]
        b += 1
    print(ls)
    return yy(ls)

   
