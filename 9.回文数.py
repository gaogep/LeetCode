#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        if strx[::-1] == strx:
            return True
        return False
