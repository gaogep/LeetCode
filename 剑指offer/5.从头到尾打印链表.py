# 输入一个链表的头节点,从尾到头反过来打印每个节点的值


class listNode:
    def __init__(self, Value, Next=None):
        self.Value = Value
        self.Next = Next

    # 反着往链表里加数
    def insertVal1(self, Value):
        next_node = listNode(Value)
        next_node.Next = self
        return next_node

    # 正着往链表里加数
    def insertVal2(self, Value):
        next_node = listNode(Value)
        while self.Next:
            self = self.Next
        self.Next = next_node


head = listNode(1)
for num in range(2, 6):
    head.insertVal2(num)


# 利用堆栈
def reversePrintl(head):
    stack = []
    while head:
        stack.append(head.Value)
        head = head.Next
    for val in stack[::-1]:
        print(val)


# 利用递归
def reversePrintr(head):
    if head:
        if head.Next:
            reversePrintr(head.Next)
        print(head.Value)


reversePrintr(head)
