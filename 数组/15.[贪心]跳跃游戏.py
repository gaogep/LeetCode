#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (34.12%)
# Total Accepted:    15K
# Total Submissions: 43.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
# 贪心算法
# 每次都标记自己能走到的最远的位置，如果还没到达终点，则对未走过的格子向前遍历；
# 如果已经没有未走过的格子，且没到达终点，则输出false；到达终点则输出true
class Solution:
    def canJump(self, nums):
        far = nums[0]                # 1.初始最远的跳跃距离
        n = len(nums)                # 2.数组的长度
        for i in range(n):           # 3.遍历索引
            if i > far:              # 4.最远距离不变了 i还在增加
                return False
            elif i + nums[i] > far:  # 5.更新最远距离
                far = i + nums[i]
        return True

s = Solution()
print(s.canJump([2,0,0,0]))

