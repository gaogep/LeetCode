# 输入一个正整数数组, 把数组里所有数字拼接起来排成一个数
# 打印能拼接出的所有数字中最小的一个.
from functools import cmp_to_key


def comparestr(a, b):
    if a+b > b+a:
        return 1
    if a+b < b+a:
        return -1
    else:
        return 0


def PrintMinNumber(arr):
    if not arr:
        return ""
    strs = list(map(str, arr))
    strs.sort(key=cmp_to_key(comparestr))
    return "".join(strs).lstrip('0') or '0'


print(PrintMinNumber([3, 32, 321]))
