# 输入两个链表，找出它们的第一个公共节点


class listNode:
    def __init__(self, Value, Next=None):
        self.Value = Value
        self.Next = Next

    def insert(self, Value):
        next_node = listNode(Value)
        while self.Next:
            self = self.Next
        self.Next = next_node


l1 = listNode(1)
l1.insert(2)
l1.insert(3)
l1.insert(6)
l1.insert(7)
l2 = listNode(4)
l2.insert(5)
l2.insert(6)


def getListLen(head):
    length = 0
    while head:
        head = head.Next
        length += 1
    return length


def forward(head, distance):
    while distance:
        head = head.Next
        distance -= 1
    return head


def findCommonNode(head1, head2):
    if not (head1 and head2):
        return

    if head1.Value == head2.Value:
        return head1

    len1 = getListLen(head1)
    len2 = getListLen(head2)
    distance = len1 - len2

    if distance < 0:
        head2 = forward(head2, distance)
    else:
        head1 = forward(head1, distance)

    while head1 and head2:
        if head1.Value == head2.Value:
            return head1
        head1 = head1.Next
        head2 = head2.Next
