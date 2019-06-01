class MinStack:
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, value):
        if not self.minStack and not self.stack:
            self.minStack.append(value)
            self.stack.append(value)
        else:
            self.stack.append(value)
            if value < self.minStack[-1]:
                self.minStack.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
        return value

    def stackMin(self):
        return self.minStack[-1]
