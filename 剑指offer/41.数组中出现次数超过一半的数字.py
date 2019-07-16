# 数组中有一个数字出现的次数超过数组长度的一半
# 请找出这个数字
arr = [1, 3, 3, 3, 3, 2, 5, 4, 3, 3, 3, 3, 3, 3, 3]


def findNumber(arr):
    if not arr:
        return
    res = arr[0]
    times = 1
    length = len(arr)
    # 找出出现频率最高的数字存入res
    for i in range(1, length):
        if times == 0:
            res = arr[i]
            times = 1

        if res == arr[i]:
            times += 1
        else:
            times -= 1

    # 确认出现频率最高的数字的出现次数超出数组长度的一半
    if length - len(set(arr)) + 1 < length // 2:
        res = None
    return res


print(findNumber(arr))
