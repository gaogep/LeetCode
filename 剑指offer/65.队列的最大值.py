# 请定义一个队列 并实现一个函数求得其最大值
# 要求函数事件复杂度为O(1)


class MaxQueue:
    def __init__(self):
        self.queue = []
        self.queue_max = []

    def pop_front(self):
        return self.queue.pop(0)

    def push_back(self, value):
        if not self.queue_max:
            self.queue_max.append(value)
        elif self.queue_max[0] < value:
            self.queue_max.pop(0)
            self.queue_max.append(value)
        self.queue.append(value)

    def get_max(self):
        return self.queue_max[0]
