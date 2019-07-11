# 在一个数组中除一个数字只出现一次之外，其他数字都出现了3次
# 请找出那个只出现一次的数字

from collections import defaultdict


def findOnce(arr):
    record = defaultdict(lambda: 0)
    for num in arr:
        record[num] += 1
    return record


# def getBitSum(num):
#     bitsum = 0
#     while num != 0:
#         if num & 1 != 0:
#             bitsum += 1
#         num = num >> 1
#     return bitsum


print(findOnce([3, 3, 3, 2, 4, 4, 4]))
