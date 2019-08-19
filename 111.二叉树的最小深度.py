#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if root.left and not root.right:
            left = self.minDepth(root.left)
            right = float("inf")
        elif root.right and not root.left:
            right = self.minDepth(root.right)
            left = float("inf")
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
        return min(left, right) + 1
