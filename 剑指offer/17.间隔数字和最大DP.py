# 从一个数组中间隔的选取一些数字 使选取的数字之和最大
lis = [1, 2, 4, 1, 7, 8, 3]


def findMax(arr):
    arrlen = len(arr)
    opt = [0 for i in range(arrlen)]
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, arrlen):
        opt[i] = max(opt[i-2] + arr[i], arr[i-1])
    return opt[-1]


print(findMax(lis))
