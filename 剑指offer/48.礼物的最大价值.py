# 在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
# 你可以从棋盘的左上角开始拿盒子里的礼物，每次向右或者向下移动一格
# 直到到达棋盘的右下角，给定一个棋盘及其上面的礼物，请你计算你最多
# 能拿到多少价值的礼物

from numpy import zeros
arr = [
    [1, 10, 3, 8],
    [12, 2, 9, 6],
    [5, 7, 4, 11],
    [3, 7, 16, 5]
]


# 动态规划->设f(i, j)为到达坐标[i,j]时能拿到礼物总和的最大值
# 当前点的礼物总价值等于前一步走下来的价值加上当前格子礼物的价值
# 譬如点[2, 3]的价格等于[1,3](上头的点) [2, 2](左边的点的)中价格的
# 最大值加上当前点[2, 3]礼物的价格
# 状态转移方程： f(i, j) = max(f(i-1, j), f(i, j-1)) + gift(i, j)


def getValuableGift(arr):
    if not arr:
        return
    rows = len(arr)
    cols = len(arr[0])
    maxvalues = zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            dw = maxvalues[i-1][j]
            rt = maxvalues[i][j-1] 
            maxvalues[i][j] = max(dw, rt) + arr[i][j]
    return maxvalues[rows-1][cols-1]


print(getValuableGift(arr))
