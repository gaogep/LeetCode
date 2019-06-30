# 输入一个递增排序的数组和一个数字s，在这个数组中查找两个数
# 使得它们的和正好是s，如果有多对数字的和等于s，则输出任意一对即可


arr = [1, 2, 4, 7, 11, 15]


# 解法1: 利用哈希表
def getSumS1(arr, s):
    if not arr:
        return
    ret = []
    hash_ = dict(zip(arr, range(len(arr))))
    for i in range(len(arr)):
        res = s - arr[i]
        if hash_.get(res):
            ret.append(res)
            ret.append(arr[i])
            break
    return ret


# 解法2: 利用最大最小值
def getSumS2(arr, s):
    if not arr:
        return
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] + arr[high] > s:
            high -= 1
        elif arr[low] + arr[high] < s:
            low += 1
        else:
            return [arr[low], arr[high]]


print(getSumS2(arr, 15))
