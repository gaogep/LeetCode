# 给定一个链表的头指针和节点指针
# 定义一个函数在o(1)时间内删除该节点


def deleteNode(head, present):
    # 1.判断删除的节点不是尾节点
    # 2.判断链表是否只有一个节点
    if present.Next:
        tmp = present.Next
        present.Value = tmp.Value
        present.Next = tmp.Next
        return head
    elif head is present:
        head = head.Next
        return head
    else:
        h = head
        while h.Next != present:
            h = h.Next
        h.Next = None
        return head
