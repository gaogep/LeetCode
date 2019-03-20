class Treeroot(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Treeroot
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res

    def inorderwithloop(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

    def postorderwithloop(self, root):
        res = []
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
            res.append(stack2.pop().val)
        return res
