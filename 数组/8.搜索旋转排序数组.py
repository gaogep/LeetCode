#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.07%)
# Total Accepted:    19.3K
# Total Submissions: 53.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
# 

# binarysearch是用来对2数组分别二分查找的。找断点比较有意思：我们通过l 和 R 求 mid， 
# 通过比较mid和最右边的r的值，我们去判断第二段递增序列的第一个点。最右边的r永远是在递增序列中，
# 如果num[mid] < num[r]，说明我们这个mid与r在同一个递增序列，我们减少r，令r=mid，缩小范围去查找断点
# 如果num[mid] > num[r]，说明mid与r在2个递增序列，增大L,令l= mid+1, 不断逼近断点。

class Solution:
    def search(self, nums, target):
        # 查找旋转点
        pass

    def binarysearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1
        

