# 实现一个函数，检查二叉树是否平衡，平衡的定义如下，对于树中的任意一个结点，
# 其两颗子树的高度差不超过1。给定指向树根结点的指针TreeNode* root，请返回一个bool，
# 代表这棵树是否平衡


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = treeNode(1)
root.left = treeNode(2)
root.left.left = treeNode(3)


def getTreeDepth(root):
    if not root:
        return 0
    left = getTreeDepth(root.left)
    right = getTreeDepth(root.right)
    return max(left, right) + 1


def isBalance(root):
    ret = True
    if not root:
        ret = False
    left_depth = getTreeDepth(root.left)
    right_depth = getTreeDepth(root.right)
    if abs(left_depth - right_depth) > 1:
        ret = False
    return ret


print(isBalance(root))
