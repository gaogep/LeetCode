#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2[:n]
        nums1.sort()
