# 把一个数组最开始的若干个元素搬到数组的末尾,我们称之为数组的旋转
# 输入一个递增排序的数组的一个旋转,输出旋转数组的最小元素.
# 例如数组[3, 4, 5, 1, 2]为[1, 2, 3, 4, 5]的一个旋转


# 利用二分查找,尽量降低时间复杂度
# 不要去从头到尾进行遍历
def rotateSmallest(arr):
    low = 0
    high = len(arr) - 1
    mid = low
    # 一旦发现第一个数字小于最后一个数字
    # 表明这个数组是排好序的 把排序数组中前面0个元素
    # 搬到了后头 所以可以立即返回
    while arr[low] >= arr[high]:
        if high - low == 1:
            mid = high
            break
        mid = (low + high) // 2

        if arr[low] == arr[high] and arr[mid] == arr[low]:
            return findInorder(arr)

        if arr[mid] >= arr[low]:
            low = mid
        elif arr[mid] <= arr[high]:
            high = mid
    return arr[mid]


# 当然也要考虑特殊情况
# 例如[0, 1, 1, 1, 1, 1]也能算是一个递增的数组
# 这时候将这个数组旋转可能变成[1, 1, 1, 1, 0, 1]
# 二分查找就失效了 只能顺序查找
def findInorder(arr):
    return min(arr)


print(rotateSmallest([3, 4, 5, 1]))
