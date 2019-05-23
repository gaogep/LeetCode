# 输入一个链表,输出该链表中倒数第k个节点.
# 为了符合大多数人的习惯,本题从1开始计数,即链表的尾节点是倒数第1个节点
# 例如,一个链表有6个节点,从头节点开始,它们的值依次是1,2,3,4,5,6.
# 这个链表的倒数第3个节点是值为4的节点


class listNode:
    def __init__(self, Value, Next=None):
        self.Value = Value
        self.Next = Next

    def insert(self, Value):
        next_node = listNode(Value)
        while self.Next:
            self = self.Next
        self.Next = next_node


head = listNode(1)
for val in range(2, 11):
    head.insert(val)


# 考虑3中特殊情况
# 1.头结点为空
# 2.k为0
# 3.k的值大于链表的总节点数


def printKnode(head, k):
    # 这里处理1、2两种情况
    if not head or k == 0:
        return None

    p1 = head
    p2 = head
    # 走k-1步
    for i in range(k-1):
        if p1.Next:  # 这里的if判断用于处理第3中情况
            p1 = p1.Next
        else:
            return None
    while p1.Next:
        p1 = p1.Next
        p2 = p2.Next

    return p2


print(printKnode(head, 3).Value)
