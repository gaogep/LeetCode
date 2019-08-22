#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#


class Solution:
    def generate(self, numRows):
        res = sub = []
        for i in range(numRows+1):
            if i == 1:
                sub = [1]
                res.append(sub)
            if i >= 2:
                tmp = []
                for j in range(len(sub)-1):
                    tmp.append(sub[j] + sub[j+1])
                sub = [1] + tmp + [1]
                res.append(sub)
        return res

print(Solution().generate(5))
