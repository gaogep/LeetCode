# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, root, x):
        if root == None:
            root = TreeNode(x)
        elif x < root.val:
            root.left = self.insert(root.left, x)
        elif x > root.val:
            root.right = self.insert(root.right, x)
        return root


# 解法一 利用栈
class BSTIterator1(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.find_min(root)

    def find_min(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        # 从栈中弹出最小元素 同是确定该节点是否有右子树
        # 因为右子树根节点比它大但其子节点要比父节点小
        tmp = self.stack.pop()
        self.find_min(tmp.right)
        return tmp.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.stack else False
        
# 解法二 利用二叉树的中序遍历
class BSTIterator2(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.que = []
        self.inorder(root)

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.que.append(root)
        self.inorder(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.que.pop(0).val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.que else False


root = TreeNode(10)
root.insert(root, 5)
root.insert(root, 12)