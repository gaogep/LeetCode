#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#


# 可对比最大子列和这一题目
class Solution:
    def maxProfit(self, prices):
        maxpro = tmp = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                maxpro += tmp
        return maxpro


# print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
