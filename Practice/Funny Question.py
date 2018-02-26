# version 3.6
# Something Funny

# Change Partner
yz = (1, 2, 3)
zd = {"a": 9, "b": 8, "c": 7}


def jiaohuan(*arg, **kwargs):
    tu = list(arg)
    dic = kwargs
    j = 0
    for i in dic.keys():
        dic[i], tu[j] = tu[j], dic[i]
        j += 1
    print(tuple(tu))
    print(dic)


# Proper or Reversed
def xul(*arg):
    arg = list(arg)
    if arg == sorted(arg):
        print("UP")
    elif arg == list(reversed(sorted(arg))):  # sort(arg,reverse=Ture)
        print("DOWN")
    else:
        print("None")


# Find some Number in a Range
li = [i * 3 for i in range(101) if i % 2 != 0]
li = [i * 3 for i in range(1, 101, 2)]
list(map(lambda x: x * 3, list(range(1, 100, 2))))
