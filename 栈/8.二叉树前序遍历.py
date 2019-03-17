class Treeroot(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Treeroot
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res

    def preorderWithloop(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            
            if stack:
                tmp = stack.pop()
                root = tmp.right
        return res