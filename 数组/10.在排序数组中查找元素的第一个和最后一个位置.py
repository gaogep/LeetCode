#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (35.39%)
# Total Accepted:    15.2K
# Total Submissions: 42.6K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
# 采用双指针法
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        elif target < nums[0] or target > nums[-1]:
            return [-1,-1]
        else:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                #当找到相等的值时，把左右指针合并并分别向左向右依次遍历找出上下限
                elif target == nums[mid]:
                    l = mid
                    r = mid
                    # 因为是排序好的数组 所以重复元素周围必定有重复元素啊
                    while l-1 >= 0 and nums[l-1] == target:
                        l -= 1
                    while r+1 <= len(nums)-1 and nums[r+1] == target:
                        r += 1
                    return [l,r]
        return [-1,-1]

