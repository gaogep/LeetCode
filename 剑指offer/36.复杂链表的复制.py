# 请事先函数ComplexListNodeClone复制一个复杂链表
# 在复杂链表中,每个节点除了有一个指向下一个节点的指针
# 外,还有一个指针指向链表中任一节点或者null


class listNode:
    def __init__(self, value, _next=None, sibling=None):
        self.value = value
        self._next = _next
        self.sibling = sibling

    def insert(self, Value):
        next_node = listNode(Value)
        while self._next:
            self = self._next
        self._next = next_node


head = listNode(1)
for val in range(2, 11):
    head.insert(val)


def complexListNodeClone(head):
    tmp = cloned = head
    while head._next:
        tmp._next = head._next
        tmp.sibling = head.sibling
        tmp = tmp._next
        head = head._next
    return cloned


c = complexListNodeClone(head)
while c._next:
    print(c.value)
    c = c._next
