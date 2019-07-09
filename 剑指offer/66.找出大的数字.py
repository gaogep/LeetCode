# 请编写一个方法，找出两个数字中最大的那个
# 条件是不得使用if-else等比较和判断运算符


def getBigger(a, b):
    b = a-b
    a -= b & (b >> 31)
    return a


print(getBigger(10, 7))
