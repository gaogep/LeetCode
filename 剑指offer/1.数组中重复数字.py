# 在一个长度为n的数组中所有的数字都在0~n-1范围内
# 找出其中重复的数字

arr = [2, 3, 1, 0, 2, 5, 3]


# 注意考虑特殊情况 如数组为空的情况
def repeat(arr):
    rep = []
    if arr:
        meet = []
        for num in arr:
            if num not in meet:
                meet.append(num)
            else:
                rep.append(num)
    return rep


# 优化->将空间复杂度降至O(1)
# 注意到数组中所有的数字都在0~n-1范围内
# 那么当数组排序之后数字i将出现在下标为i的地方
# 从头到尾扫描数组中的每个数字 当扫描到下标为i
# 的数字的时候先看这个数字等不等于i 如果是 往后扫描
# 如果不是 看arr[arr[i]]这个地方的数字是否和arr[i]相等
# 相等就重复了 直接跳出 不相等的话两边互换 继续查找
def repeat_optimize(arr):
    res = []  # 防止重复元素被添加多次
    if arr:
        for i in range(len(arr)):
            while arr[i] != i:
                t = arr[i]
                # 判断索引和该索引上的数字是否相等
                if arr[i] == arr[t]:
                    res.append(arr[i])
                    break
                arr[i], arr[t] = arr[t], arr[i]
    return []
