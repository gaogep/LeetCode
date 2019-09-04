#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# 相当于间隔数字最大和


class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        opt = [0 for i in range(len(nums))]
        opt[0] = nums[0]
        opt[1] = max(nums[1], opt[0])
        for j in range(2, len(nums)):
            opt[j] = max(opt[j-2]+nums[j], opt[j-1])
        return opt[-1]
