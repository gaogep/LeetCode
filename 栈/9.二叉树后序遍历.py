class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res

    def postorderWithloop(self, root):
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