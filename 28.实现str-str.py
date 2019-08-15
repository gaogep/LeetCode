#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#


class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        p1 = 0
        while p1 < len(haystack):
            if haystack[p1] != needle[0]:
                p1 += 1
            elif haystack[p1:p1+len(needle)] == needle:
                return p1
            else:
                p1 += 1
        return -1


print(Solution().strStr("", "issip"))
