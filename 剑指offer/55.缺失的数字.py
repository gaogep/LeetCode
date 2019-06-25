# 0-n-1缺失的数字
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在0-n-1的范围内
# 在范围0-n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字

arr = [0, 1, 2, 3, 5, 6, 7, 8, 9]


# 解法1: 利用数组和
def findNumber1(arr):
    sum_of_arr = (arr[0] + arr[-1]) * len(arr) // 2
    return sum_of_arr - sum(arr)


# 解法2: 二分查找
def findNumber2(arr, n):
    if not arr:
        return
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            low = mid + 1
        elif arr[mid] != mid and arr[mid-1] != mid - 1:
            high = mid - 1
        elif arr[mid] != mid and arr[mid-1] == mid - 1:
            return mid


print(findNumber2(arr, 10))
