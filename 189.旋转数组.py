#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#


class Solution:
    def rotate(self, nums, k):
        # 旋转数组k次，k%n个尾部元素会被移动到头部
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
