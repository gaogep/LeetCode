#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        while n >= 5:
            n = n // 5
            ret += n
        return ret
