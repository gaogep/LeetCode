#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (34.61%)
# Total Accepted:    14.5K
# Total Submissions: 41.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        

