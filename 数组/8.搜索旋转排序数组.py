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
# 本题的思路在于利用二分查找查找两个有序的序列
# 其关键点在于找到第二个有序序列的其实位置
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 先找到两个第二个升序数组的第一项的index
        l = 0
        r = len(nums) -1
        while l < r:
            mid = (l + r)//2
            # 首先要明白的是最右边的指针永远处在一个递增序列中
            # 如果中间的数字比右边的大 那么mid与r处在两个递增序列之中
            # 将左指针赋值为　mid + 1　继续寻找第二个序列的第一项
            if nums[mid] > nums[r]:
                l = mid + 1
            # 如果中间的数字比右边的小 说明二者处在同一个递增的序列中
            # 那么就要缩小右指针的范围　令 r = mid
            else:
                r = mid

        pol = l
        ans = self.binary_search(target, nums[:pol])
        if ans == -1:
            ans = self.binary_search(target, nums[pol:])
            if ans != -1:
                ans += len(nums[:pol])
 
        return ans
    
    def binary_search(self, target, nums):
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
        return index

s = Solution()
s.search([4, 5, 6, 7, 0, 1, 2], 7)
