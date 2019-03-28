#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (21.51%)
# Total Accepted:    43.7K
# Total Submissions: 202.2K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 我们可以先对数组进行排序，如果是计算两个元素的和的话，我们会分别设置头和尾两个指针
# 向中间靠拢，那么三个的话，我们只需要先对第一个数进行循环取值下标i
# 剩下的两个指针分别指向i+1和数组的最后一个元素
# 这样的复杂度是 排序O(nlogn) + 查找O(n^2) = O(n^2)
# 
class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        result = []
        isvisited = []
        for i, a in enumerate(nums):
            if a in isvisited: # 去除重复元素
                continue
            else:
                isvisited.append(a)
            tmp = set()
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                sum_val = a + b + c
                if sum_val == 0:
                    if len(tmp) >= 1 and (b in tmp): # 去除剩余元素中的重复元素
                        pass
                    else:
                        result.append([a, b, c])
                        tmp.add(a)
                        tmp.add(b)
                        tmp.add(c)
                    left += 1
                    right -= 1
                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1
        return result

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
