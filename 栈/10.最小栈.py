class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self._stack or self._stack[-1] >= x:
            self._stack.append(x)
 

    def pop(self):
        """
        :rtype: None
        """
        if self.stack and self._stack and self.stack[-1] == self._stack[-1]:
            del self._stack[-1]
        if self.stack:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self._stack:
            return self._stack[-1]
            