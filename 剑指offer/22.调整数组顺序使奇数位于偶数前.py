# 输入一个整数数组,实现一个函数来调整该数组中数字的顺序
# 使得所有奇数位于数组的前半部分,所有偶数位于数组的后半部分


def adjustArray(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        while low < high and (arr[low] & 1) != 0:
            low += 1
        while low < high and (arr[high] & 1) == 0:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
    return arr


print(adjustArray([1, 2, 3, 4, 5]))
