# version 3.6
# 测试type 和 isinstance 那个的速度更快

import time


def time_kick(func):
    def new_fun(*args, **kwargs):
        t0 = time.time()

        # print('star time: %s'%(time.strftime('%x',time.localtime())) )

        back = func(*args, **kwargs)

        # print('end time: %s'%(time.strftime('%x',time.localtime())) )

        s = time.time() - t0

        return s

    return new_fun


@time_kick
def type_sp():
    for i in range(1000000):
        type(i) == int


@time_kick
def isin_sp():
    for i in range(1000000):
        isinstance(1, (int, float, str))


def kuai():
    a = type_sp()

    b = isin_sp()

    if a < b:  # 小的更快

        print('type更快')

    else:

        print('isinstance更快')


kuai()
