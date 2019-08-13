#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
