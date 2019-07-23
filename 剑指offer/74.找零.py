def findChanges(cost):
    nums, rest = 0, 1024 - cost
    for i in range(6, -1, -2):
        num, rest = getCoins(i, rest)
        nums += num
    return nums


def getCoins(bits, rest):
    coins = rest >> bits
    rest -= coins << bits
    return coins, rest


print(findChanges(200))
