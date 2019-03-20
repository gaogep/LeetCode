class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        # 注意 中序遍历和后续遍历的数组大小是相同的
        root.left = self.buildTree(inorder[:index], postorder[:index])
        # 注意这里 postorder[index:-1] 的作用是剔除掉最后一个根节点
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root 
