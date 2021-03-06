#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not (p and q):
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(q.left, p.left)
        right = self.isSameTree(q.right, p.right)

        return left and right
