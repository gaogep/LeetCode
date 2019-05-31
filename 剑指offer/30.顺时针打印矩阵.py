# 输入一个矩阵, 按照从外向里一顺时针的顺序
# 依次打印出每一个数字
# 例如如下矩阵打印结果为: 1 2 3 4 8 12 16 15 14 13.....11 10
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def printMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if not matrix or not rows or not cols:
        return
    start = 0
    while cols > (start << 1) and rows > (start << 1):
        printCore(matrix, rows, cols, start)
        start += 1


def printCore(matrix, rows, cols, start):
    endX = cols - 1 - start
    endY = rows - 1 - start

    # 从左到右打印一行
    # 完成此项打印的前提条件: 矩阵至少有一行
    for i in range(start, endX+1):
        print(matrix[start][i])

    # 从上到下打印一行
    # 完成此项打印的前提条件: 终止行号大于起始行号
    if start < endY:
        for i in range(start+1, endY+1):
            print(matrix[i][endX])

    # 从右到左打印一行
    # 完成此项打印的前提条件: 矩阵至少有两行两列
    # 即终止行号大于起始行号 终止列号大于起始列号
    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            print(matrix[endY][i])

    # 从下到上打印一行
    # 完成此项打印的前提条件: 矩阵至少有三行两列
    # 即终止行号至少比起始行号大2 终止列号大于起始列号
    if start < endX and start < endY - 1:
        for i in range(endY-1, start, -1):
            print(matrix[i][start])


printMatrix(matrix)
