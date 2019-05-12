# 根据二叉树的前序和中序遍历结果重建二叉树


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not inorder:
        return None
    root = treeNode(preorder[0])
    pos = inorder.index(preorder[0])
    lefttree = inorder[:pos]
    righttree = inorder[pos+1:]
    preorder.pop(0)
    root.left = buildTree(preorder, lefttree)
    root.right = buildTree(preorder, righttree)
    return root


root = buildTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
