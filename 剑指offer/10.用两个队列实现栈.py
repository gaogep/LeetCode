class QueueStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, value):
        self.q1.append(value)

    def pop(self):
        ret = "The stack is empty"
        if not self.q1 and not self.q2:
            return ret
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            ret = self.q1.pop(0)
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            ret = self.q2.pop(0)
        return ret
