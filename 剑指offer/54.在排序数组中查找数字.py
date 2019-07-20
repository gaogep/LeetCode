# 数字在排序数组中出现的次数
# 统计一个数字在排序数组中出现的次数
# 二分查找 找到第一个和最后一个数字的位置 然后相减
arr = [1, 2, 2, 3, 3, 3, 3, 4, 5]


def getFirstValue(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            # 往前找
            if arr[mid-1] != k:
                return mid
            else:
                high = mid


def getLastValue(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            # 往后找
            if arr[mid+1] != k:
                return mid
            else:
                low = mid


def countNumberTimes(arr, k):
    times = 0
    if arr:
        times = getLastValue(arr, k) - getFirstValue(arr, k) + 1
    return times


print(countNumberTimes(arr, 3))
