#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


class Solution:
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        lis = s.split()
        if not lis:
            return 0
        return len(lis[-1])
