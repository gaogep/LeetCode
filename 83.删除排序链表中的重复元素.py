#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = head
        while start and start.next:
            while start and start.next and start.val != start.next.val:
                start = start.next
            tmp = start.next
            if tmp:
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                start.next = tmp.next
                start = start.next
        return head


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(3)
# print(Solution().deleteDuplicates(head).val)
