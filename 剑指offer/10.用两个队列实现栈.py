class qStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, value):
        self.queue1.append(value)

    def pop(self):
        ret = "The stack is empty"
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            ret = self.queue1.pop(0)
        return ret
