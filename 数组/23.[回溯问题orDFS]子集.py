#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        nums.sort()
        self.bracktrack(list, [], nums, 0)
        return list

    def bracktrack(self, list, tempList, nums, start):
        list.append(tempList.copy())
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            self.bracktrack(list, tempList, nums, i + 1)
            tempList.pop()   
