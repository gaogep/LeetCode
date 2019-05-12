# 在一个二维数组中, 每一行都按照从左到右递增的顺序排序
# 每列都按照从上到下递增的顺序排序.请完成一个函数,输入这样的
# 一个二维数组和一个整数,判断数组中是否含有该整数

matrix = [
            [1, 2, 10, 14],
            [2, 4, 11, 15],
            [4, 7, 12, 16],
            [6, 8, 13, 17]
         ]


# 从右上角开始寻找
# 后续思路类似于二分查找
# 如果右上角的数字大于查找的数字,右上角数字所在的那一列可以剔除
# 如果右上角的数字小于查找的数字,那么就往下方寻找
# 不断缩小查找范围,层层逼近要查找的数字
def findNumber(matrix, num):
    found = False
    if matrix:
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == num:
                found = True
                break
            elif matrix[row][col] > num:
                col -= 1
            else:
                row += 1
    return found


print(findNumber(matrix, 7))
