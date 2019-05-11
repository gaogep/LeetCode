class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 若中序遍历结果为空 说明为空树
        if not inorder:
            return None
        # 根据前序遍历的结果获取根节点
        root = TreeNode(preorder[0])
        # 在中序遍历的结果中找到根节点的位置
        index = inorder.index(preorder[0])
        # 中序遍历结果中 根节点的左侧为左子树的中序遍历结果
        left_tree = inorder[:index]
        # 中序遍历结果中 跟几点的右侧为右子树的终须遍历结果
        right_tree = inorder[index+1:]
        # 在前序遍历的结果中删除根节点
        preorder.pop(0)
        # 根据左右子树的前序遍历结果构造二叉树
        root.left = self.buildTree(preorder, left_tree)
        root.right = self.buildTree(preorder, right_tree)

        return root


s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
