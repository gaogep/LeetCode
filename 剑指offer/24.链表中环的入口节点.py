# 如果一个链表中包含环,如何找出环的入口节点?
#           -------------
#          |            |
# 1-> 2 -> 3-> 4 ->5 -> 6


class listNode:
    def __init__(self, Value, Next=None):
        self.Value = Value
        self.Next = Next


h1 = listNode(1)
h2 = listNode(2)
h3 = listNode(3)
h4 = listNode(4)
h5 = listNode(5)
h6 = listNode(6)

h1.Next = h2
h2.Next = h3
h3.Next = h4
h4.Next = h5
h5.Next = h6
h6.Next = h3


def meetingNode(head):
    if not head:
        return
    # 设置快慢两个指针
    # pslow一次走一步
    # pfast一次走两步
    # 如果二者最终能相遇
    # 那么说明这个链表包含环
    ps = head.Next
    if not ps:
        return None
    pf = ps.Next

    while pf and ps:
        # 如果链表中包含环
        # 那么两个指针必定在环中某个节点相遇
        if pf == ps:
            return pf

        ps = ps.Next
        pf = pf.Next
        if pf:
            pf = pf.Next
    return


def findEntry(head):
    mnode = meetingNode(head)
    if not mnode:
        return

    # 得到环中节点的个数
    circleNodes = 1
    tmp = mnode
    while tmp.Next != mnode:
        circleNodes += 1

    # 先移动p1指针
    p1 = head
    while circleNodes != 0:
        p1 = p1.Next
        circleNodes -= 1

    p2 = head
    # 再同时以相同的速度移动p1 p2指针
    while p1 != p2:
        p1 = p1.Next
        p2 = p2.Next

    return p1  # 返回环的入口节点
