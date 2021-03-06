#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
# https://leetcode-cn.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (47.36%)
# Total Accepted:    1.8K
# Total Submissions: 3.8K
# Testcase Example:  '[1,2,1]'
#
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x
# 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#
# 示例 1:
#
#
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
#
#
# 注意: 输入数组的长度不会超过 10000。
#
#
from copy import deepcopy


class Solution:
    # 于循环数组的问题一个常见的处理手段就是通过余数，然后将数组的长度扩大两倍即可
    def nextGreaterElements(self, nums):
        stack = []
        nums_len = len(nums)
        res = [-1] * nums_len
        for i in range(nums_len*2):
            while stack and nums[stack[-1]] < nums[i % nums_len]:
                res[stack.pop()] = nums[i % nums_len]
            stack.append(i % nums_len)
        return res


s = Solution()
print(s.nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))
# [120,11,120,120,123,123,-1,100,100,100]
