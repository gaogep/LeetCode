#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#


class Solution:
    def convertToTitle(self, n):
        res = ''                            # 结果
        while n:                            # 当商大于0时
            n -= 1                          # 要先减1才能找到对应的数字
            r, n = n % 26, n // 26          # 获取当前的商和余数
            res = chr(65+r) + res           # 寻找当前位对应的字符，加入到结果的最高位
        return res


print(Solution().convertToTitle(1111333))
