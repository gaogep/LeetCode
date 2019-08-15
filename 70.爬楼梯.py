#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


class Solution:
    def climbStairs(self, n):
        if n < 2:
            return [0, 1, 2][n]
        a = 1  # f(1)
        b = 2  # f(2)
        for i in range(3, n+1):
            a, b = b, a + b
        return b
