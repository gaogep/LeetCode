#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (39.39%)
# Total Accepted:    19.9K
# Total Submissions: 50.4K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 
#


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i, a in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                tmp = a + b + c
                if abs(res - target) > abs(tmp - target):
                    res = tmp
                elif target < tmp:
                    right -= 1
                else:
                    left += 1
        return res
