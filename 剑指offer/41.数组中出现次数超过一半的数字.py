# 数组中有一个数字出现的次数超过数组长度的一半
# 请找出这个数字
arr = [1, 3, 3, 3, 3, 2, 5, 4, 3, 3, 3, 3, 3, 3, 3]


def find_half_number(arr):
    if not arr:
        return
    times, ret = 1, arr[0]
    for num in arr:
        if times == 0:
            times, ret = 1, num
        if ret == num:
            times += 1
        else:
            times -= 1
    if len(arr) - len(set(arr)) + 1 < len(arr) // 2:
        ret = None
    return ret


print(find_half_number(arr))
