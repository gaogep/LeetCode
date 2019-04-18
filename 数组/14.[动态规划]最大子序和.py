#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.43%)
# Total Accepted:    49.2K
# Total Submissions: 111.5K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
# 动态规划
class Solution:
    def maxSubArray(self, nums) -> int:
        ThisSum = 0
        MaxSum = nums[0]
        for i in range(len(nums)):
            ThisSum += nums[i]    # 向右累加
            if ThisSum > MaxSum: 
                MaxSum = ThisSum  # 发现更大的和更新结果
            elif ThisSum < 0:     # 如果当前子列和为负
                ThisSum = 0       # 则不可能使后面的部分和增大 抛弃之
        return MaxSum

