#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#


class Solution:
    def twoSum(self, numbers, target):
        result = []
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] < target:
                start += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                result.append(start+1)
                result.append(end+1)
                break
        return result


# print(Solution().twoSum([2, 7, 11, 15], 9))
