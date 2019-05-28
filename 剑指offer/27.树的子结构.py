# 输入两棵二叉树A和B,判断B是不是A的子结构


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 1.首先在一棵树中找到另一棵树的根节点
def hasSubtree(root1, root2):
    res = False
    if root1 and root2:
        if root1.value == root2.value:
            res = isChildren(root1, root2)
        if not res:
            res = hasSubtree(root1.left, root2)
        if not res:
            res = hasSubtree(root1.right, root2)
    return res


# 2.判断找到的根节点来判断一棵树是否包含另一棵树
def isChildren(root1, root2):
    if not root2:
        return True

    if not root1:
        return False

    if root1.value != root2.value:
        return False

    return isChildren(root1.left, root2.left) and \
        isChildren(root1.right, root2.right)
