#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        minimum = prices[0]
        for i in prices:
            minimum = min(i, minimum)
            profit = max(i - minimum, profit)
        return profit


print(Solution().maxProfit([1, 4, 1, 4, 3, 1]))
