def cntone1(num):
    """"最初的解法"""
    cnt = 0
    while num:
        if num & 1:
            cnt += 1
        num = num >> 1
    return cnt


def cntone2(num):
    """优化的解法,避免负数的无限循环"""
    cnt = 0
    flg = 1
    while flg < num:
        if num & flg:
            cnt += 1
        flg = flg << 1
    return cnt


def cntone3(num):
    """
    最终解法
    把一个整数减去1然后和原整数做与运算
    会把该整数最右边的1变成0 那么一个二
    进制数有多少个1就能进行多少次这种运算
    """
    cnt = 0
    while num:
        cnt += 1
        num = (num - 1) & num
    return cnt


print(cntone3(105))
