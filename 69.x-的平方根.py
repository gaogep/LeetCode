#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


class Solution:
    def mySqrt(self, x: int) -> int:\
        # 牛顿迭代法
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)
