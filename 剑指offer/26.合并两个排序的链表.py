# 输入两个递增的排序链表,合并这两个链表
# 并使新链表中节点仍然是递增排序的


class listNode:
    def __init__(self, Value, Next=None):
        self.Value = Value
        self.Next = Next

    def insert(self, Value):
        next_node = listNode(Value)
        while self.Next:
            self = self.Next
        self.Next = next_node


h1 = listNode(1)
for val in range(3, 8, 2):
    h1.insert(val)

h2 = listNode(2)
for val in range(4, 9, 2):
    h2.insert(val)


def mergeList(head1, head2):
    thead = tp = listNode(-1)
    while head1 and head2:
        if head1.Value >= head2.Value:
            tp.Next = head2
            head2 = head2.Next
            tp = tp.Next
        else:
            tp.Next = head1
            head1 = head1.Next
            tp = tp.Next

    if head1:
        tp.Next = head1
    if head2:
        tp.Next = head2

    return thead


head = mergeList(h1, h2)
