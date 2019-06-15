# 输入一个整数n, 求1~n这n个整数的十进制表示中1出现的次数
# 例如,输入12 1-12这些整数中包含1的数字有 1 10 11 12 1一共出现了5次


def countOne(num):
    timesofone = 0
    for val in range(1, num+1):
        s = str(val)
        timesofone += s.count('1')
        s = ''
    return timesofone


print(countOne(100))
