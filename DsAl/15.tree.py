class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def preorderr(self, root):
        if root:
            print(root.value)
            self.preorderr(root.left)
            self.preorderr(root.right)

    def inorderr(self, root):
        if root:
            self.inorderr(root.left)
            print(root.value)
            self.inorderr(root.right)

    def postorderr(self, root):
        if root:
            self.postorderr(root.left)
            self.postorderr(root.right)
            print(root.value)

    def preorderl(self, root):
        stack = []
        while root or stack:
            while root:
                print(root.value)
                stack.append(root)
                root = root.left
            if stack:
                tmp = stack.pop()
                root = tmp.right

    def inorderl(self, root):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                tmp = stack.pop()
                print(tmp.value)
                root = tmp.right

    def postorderl(self, root):
        stack1 = []
        stack2 = []
        while root or stack1:
            while root:
                stack1.append(root)
                stack2.append(root)
                root = root.right
            if stack1:
                tmp = stack1.pop()
                root = tmp.left
        while stack2:
            print(stack2.pop().value)

    def level(self, root):
        queue = []
        queue.append(root)
        while queue:
            tmp = queue.pop(0)
            print(tmp.value)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)


root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.left.right = treeNode(5)
root.right.left = treeNode(6)
root.right.right = treeNode(7)

root.level(root)
