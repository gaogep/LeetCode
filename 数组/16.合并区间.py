#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (35.06%)
# Total Accepted:    12.9K
# Total Submissions: 36.4K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
# 思路: 先排序 然后比较区间
class Solution:
    def merge(self, intervals):
        result = []
        if len(intervals) <= 1:
            return intervals
        else:   # 以每个小区间的第一个数进行排序 那么只需要比较前一个区间的最后一个数和第二个区间的第一个数
            intervals.sort(key=lambda x: x.start)
            result.append(intervals[0])
            for i in range(1, len(intervals)):      
                prev = result[-1]                  # 如果第一个区间的最后一个数大于第二个区间的第一个数
                if intervals[i].start <= prev.end: # 那么就要进行判断 选出重合区间的边界
                    prev.end = max(prev.end, intervals[i].end)
                else:                              # 如果第一个区间的最后一个数小于第二个区间的第一个数 那么肯定不重合
                    result.append(intervals[i])
        return result
