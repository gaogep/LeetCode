class bsTreeNote:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, root, value):
        if not root:
            root = bsTreeNote(value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        return root

    def findMin(self, root, value):
        if root:
            while root.left:
                root = root.left
        return root

    def delNode(self, root, value):
        if not root:
            return
        if value < root.value:
            root.left = self.delNode(root.left, value)
        elif value > root.value:
            root.right = self.delNode(root.right, value)
        else:
            if root.left and root.right:
                tmp = self.findMin(root.right)
                root.value = tmp.value
                root.right = self.delNode(root.right, tmp.value)
            elif not (root.left and root.right):
                root = None
            elif root.left:
                root = root.left
            else:
                root = root.right
        return root


root = bsTreeNote(5)
root.insertt(4)
root.insertt(3)
root.delNode(root, 3)
