class cQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, value):
        self.stack1.append(value)
    
    def dequeue(self):
        ret = "The queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            try:
                ret = self.stack2.pop()
            except IndexError:
                pass
        else:
            ret = self.stack2.pop()
        return ret
