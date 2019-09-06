#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val):
        if not head:
            return
        pre = cur = head
        while True:
            while cur.val != val and cur.next:
                pre = cur
                cur = cur.next
            if cur.val == val and cur.next:
                pre.next = cur.next
                cur = cur.next
            elif cur.val == val and not cur.next:
                if pre.val == cur.val:
                    head = None
                else:
                    pre.next = None
                break
            else:
                break
        return head
