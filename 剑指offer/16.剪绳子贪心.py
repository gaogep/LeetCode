# 给你一根长度为n的绳子,请把绳子剪成m段,每段绳子的长度(n > 1 m > 1)
# 记为k[0] k[1] ... k[m] 请问k[0] * k[1] * ... k[m]
# 可能的最大乘积是多少?


def cut_greedy(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    # 尽可能多去剪长度为3的绳子
    timesof3 = length // 3

    # 当绳子最后剩下的长度为４的时候 不能再去减长度为3的绳子段
    # 此时更好的方法是把绳子剪成长度为2的两段 因为 2*2 > 3*1   
    if length - timesof3 * 3 == 1:
        timesof3 -= 1
    timesof2 = (length - timesof3 * 3) // 2

    return (3**timesof3) * (2**timesof2)
