#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#


class Solution:
    def singleNumber(self, nums):
        hash_ = {}
        for num in nums:
            val = hash_.get(num, -1)
            if val == -1:
                hash_[val] == 1
            else:
                hash_.pop(num)

        for num in hash_.values():
            return num
