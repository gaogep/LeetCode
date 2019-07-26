# 根据二叉树的前序和中序遍历结果重建二叉树


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rebuild(preorder, inorder):
    if not inorder:
        return
    root = treeNode(preorder[0])
    pos = inorder.index(preorder.pop(0))
    root.left = rebuild(preorder, inorder[:pos])
    root.right = rebuild(preorder, inorder[pos+1:])
    return root


root = buildTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
