# 地上有一个m行n列的方格,一个机器人从坐标(0, 0)的格子开始
# 移动,它可以每次向上下左右移动一格,但不能进入行坐标和列坐标
# 之和大于K的格子.例如,当K为18的时候,机器人能够进入方格
# (35, 37),因为3+5+3+7=18.但它不能进入方格(35, 38)
# 因为3+5+3+8=19,请问该机器人能够到达多少个给子


def movingCount(rows, cols, k):
    if k < 0 or rows <= 0 or cols <= 0:
        return 0
    visited = [[False for col in range(cols)] for row in range(rows)]
    cnt = movingCountCore(rows, cols, 0, 0, k, visited)
    return cnt


def movingCountCore(rows, cols, row, col, k, visited):
    cnt = 0
    if row >= 0 and row <= rows and col >= 0 and col <= rows \
            and getDigitSum(row) + getDigitSum(col) <= k and  \
            not visited[row][col]:

        visited[row][col] = True
        cnt = 1 + movingCountCore(rows, cols, row-1, col, k, visited) \
                + movingCountCore(rows, cols, row+1, col, k, visited) \
                + movingCountCore(rows, cols, row, col-1, k, visited) \
                + movingCountCore(rows, cols, row, col+1, k, visited)
    return cnt


def getDigitSum(num):
    dsum = 0
    while num > 0:
        dsum += num % 10
        num /= 10
    return dsum
