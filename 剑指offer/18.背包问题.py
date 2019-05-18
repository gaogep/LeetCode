# 假设我们有n件物品，分别编号为1, 2...n. 其中编号为i的物品价值为vi
# 它的重量为wi.为了简化问题，假定价值和重量都是整数值。现在，假设我
# 们有一个背包，它能够承载的重量是W.现在，我们希望往包里装这些物品
# 使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？


import numpy as np


def bagProblem(vlist, wlist, limitw):
    """"
    假定我们定义一个函数c[i, w]表示到第i个元素为止，在限制总重量为w的情况下我
    们所能选择到的最优解.那么这个最优解要么包含有i这个物品，要么不包含，肯定是这
    两种情况中的一种.如果我们选择了第i个物品，那么实际上这个最优解是c[i-1, w-wi]+vi
    而如果我们没有选择第i个物品，这个最优解是c[i-1, w]
    """
    res = np.zeros((len(vlist)+1, limitw+1), dtype=np.int32)
    for i in range(1, len(vlist)+1):
        for j in range(1, limitw+1):
            if wlist[i] <= j:
                v1 = res[i-1, j-wlist[i]] + vlist[i]
                v2 = res[i-1, j]
                res[i, j] = max(v1, v2)
            else:
                res[i, j] = res[i-1, j]
    return res[-1, -1]
