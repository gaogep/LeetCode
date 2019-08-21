#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, ssum):
        if not root:
            return False
        if not root.left and not root.right:
            return ssum == root.val
        return self.hasPathSum(root.left, ssum - root.val) or \
            self.hasPathSum(root.right, ssum - root.val)
