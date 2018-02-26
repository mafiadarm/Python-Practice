#version 3.6
#斐波拉契数生成器
def pro(num):
    n,a,b = 0,0,1
    while n < num:
        print(b)
        if n%10 ==0:
            yield
            
        a,b = b, a+b
        n = n +1
