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


def mergeAscList(head1, head2):
    new_head = listNode(-1)
    tmp = new_head
    while head1 and head2:
        if head1.Value > head2.Value:
            tmp.Next = listNode(head2.Value)
            tmp = tmp.Next
            head2 = head2.Next
        else:
            tmp.Next = listNode(head1.Value)
            tmp = tmp.Next
            head1 = head1.Next

    if head1:
        tmp.Next = head1
    if head2:
        tmp.Next = head2

    return new_head.Next


new = mergeAscList(h1, h2)
tmp = new

for i in range(8):
    print(tmp.Value)
    tmp = tmp.Next
