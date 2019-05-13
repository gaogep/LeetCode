# 上台阶一次可以上1级,也可以上2级
# 上n级的台阶有多少种解法
# 根据题意可得递推公式 当n > 2时f(n) = f(n-1) + f(n-2)
# f(0)=0 f(1)=1 f(2)=2
# 和斐波那契数列一样求解


def climb(n):
    res = [0, 1, 2]
    if n <= 2:
        return res[n]
    a = 1
    b = 2
    for i in range(3, n+1):
        s = a + b
        a = b
        b = s
    return s
