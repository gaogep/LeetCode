# 定义一个函数,输入一个链表的头结点
# 反转该链表并输出反转后链表的头结点


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


def reverseList(Head):
    # 1.头节点为空的情况
    if not Head:
        return None

    head = Head
    prev = None
    rear = Head.Next
    # 2.只有1个节点的情况
    if not rear:
        return Head

    # 3.有多个节点的情况
    while rear:
        # 当反转头节点的时候 头节点变尾节点
        # 要将头结点的下一个节点置为空
        if not prev:
            head.Next = None
        prev = head
        head = rear
        rear = rear.Next
        head.Next = prev

    return head


new_head = reverseList(head)
head = None
