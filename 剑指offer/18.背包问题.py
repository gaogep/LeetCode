# 假设我们有n件物品，分别编号为1, 2...n. 其中编号为i的物品价值为vi
# 它的重量为wi.为了简化问题，假定价值和重量都是整数值。现在，假设我
# 们有一个背包，它能够承载的重量是W.现在，我们希望往包里装这些物品
# 使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？

import numpy as np


# 函数c[i, w]表示到第i个元素为止，在限制总重量为w的情况下我们所能选择到的最优解
# 那么这个最优解要么包含有i这个物品，要么不包含，肯定是这两种情况中的一种
def solve(vlist, wlist, totalWeight, totalLength):
    ret = np.zeros((totalLength+1, totalWeight+1), dtype=np.int32)
    for i in range(1, totalLength+1):
        for j in range(1, totalWeight+1):  # i表示第几件物品, j表示背包的总重量
            if wlist[i] <= j:              # 如果第i件物品的总重量没有超过限制，选它！
                select_i = ret[i-1, j-wlist[i]] + vlist[i]
                nselect_i = ret[i-1, j]
                ret[i, j] = max(select_i, nselect_i)
            else:                          # 如果第i件物品的总重量超过限制，不选它！
                ret[i, j] = ret[i-1, j]
    return ret[-1, -1]


v = [0, 60, 100, 120]
w = [0, 10, 20, 30]
n, weight = 3, 50
print(solve(v, w, weight, n))
