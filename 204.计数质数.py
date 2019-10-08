#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start

from math import sqrt


class Solution:
    def countPrimes(self, n):
        cnt = 0
        for i in range(1, n):
            if self.isPrime(i):
                cnt += 1
        return cnt

    def isPrime(self, num):
        if num == 1:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

        # @lc code=end

print(Solution().countPrimes(999983))  # 超时 可用厄拉多塞筛法
