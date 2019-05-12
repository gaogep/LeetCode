class Treeroot(object):
    def __init__(self, x):
        self.val = x
        self.left = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        que = []
        if root:
            que.append(root)
        
        depth = 0
        while que:
            level = 0
            length = len(que)
            while level < length:
                tmp = que.pop(0)
                if tmp.left:
                    que.append(tmp.left)
                if tmp.right:
                    que.append(tmp.right)
                level += 1
            depth += 1
        return depth
