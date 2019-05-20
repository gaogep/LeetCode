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
    """最终解法"""
    cnt = 0
    while num:
        cnt += 1
        num = (num - 1) & num
    return cnt


print(cntone3(105))
