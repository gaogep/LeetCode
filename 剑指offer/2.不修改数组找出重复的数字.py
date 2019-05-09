# 在一个长度为n+1的数组中 所有的数字都在1到n的范围内(即长度为8的数组中最大值为7)
# 所以数组中至少有一个数字是重复的 请找出数组中任意一个重复的数字
# 但不要修改数组

# 例如 如果输入长度为8的数组[2, 3, 5, 4, 3, 2, 6, 7]
# 那么对应的输出应该是重复的数字2或3

rep_arr = [2, 3, 5, 4, 3, 2, 6, 7]


# 借助辅助数组,将数字m放到辅助数组索引为m的位置
def findRepNoModify1(arr):
    res = []
    tmp = [0 for i in range(len(arr))]
    for num in arr:
        if tmp[num]:
            res.append(num)
            continue
        tmp[num] = num
    return res


# 利用二分查找思想对要查找的数字进行拆分
# 例如数组长度为8 开始就是1 结束就是7 中间值为4
def findRepNoModify2(arr):
    arrlen = len(arr)
    if arrlen > 1:
        start = 1
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) >> 1
            # 计算[start, mid]数字之间的数目
            # 根据cnt得到重复数字区间
            cnt = cntRange(arr, start, mid)

            # 当只取到一个数字时，如果该数字出现数目大于1，就是重复数字
            if start == end:
                if cnt > 1:
                    return start
                else:
                    break
            # 如果count数目 > 中间数字到起始数字之差
            # 一定存在重复数字，继续在这一段中求中间数比较
            if cnt > mid - start + 1:
                end = mid
            # 否则在后一段中求中间数比较
            else:
                start = mid + 1
    return None


def cntRange(arr, start, end):
    cnt = 0
    for num in arr:
        if start <= num <= end:
            cnt += 1
    return cnt
