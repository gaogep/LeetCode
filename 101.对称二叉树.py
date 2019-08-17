#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode):
        return self.judge(root, root)

    def judge(self, r1, r2):
        if not r1 and not r2:
            return True

        if not (r1 and r2):
            return False

        if r1.val != r2.val:
            return False

        return self.judge(r1.left, r2.right) and \
            self.judge(r1.right, r2.left)
