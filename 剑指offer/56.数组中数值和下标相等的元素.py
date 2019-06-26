# 假设一个单调递增的数组中里的每个元素都是整数并且是唯一的
# 请编程实现一个函数，找出数组中任意个数值等于其下标的元素

arr = [-3, -1, 1, 3, 5]


def findIndexEqNumber(arr):
    if not arr:
        return
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return arr[mid]
        elif arr[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1


print(findIndexEqNumber(arr))
