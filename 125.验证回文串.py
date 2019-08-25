#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


class Solution:
    def isPalindrome(self, s):
        s = list(filter(str.isalnum, s.lower()))
        return True if s == s[::-1] else False
