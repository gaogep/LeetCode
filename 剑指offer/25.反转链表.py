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
for val in range(2, 6):
    head.insert(val)


def reverseList(head):
    # 处理头结点为空或者只包含头结点的情况
    if not (head and head.Next):
        return head

    pre = None
    cur = head
    while cur:
        rear = cur.Next
        cur.Next = pre
        pre = cur
        cur = rear

    return pre


head = reverseList(listNode(1))
print(head.Value)
