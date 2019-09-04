#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#


class Solution:
    def isHappy(self, n):
        unhappy = {4, 16, 37, 58, 89, 145, 42, 20}
        sumn = self.split_sum(n)
        while sumn not in unhappy:
            n = sumn
            sumn = self.split_sum(n)
            if sumn == 1:
                return True
        return False

    def split_sum(self, n):
        strn = str(n)
        sumn = 0
        for i in range(len(strn)):
            sumn += int(strn[i])**2
        return sumn
