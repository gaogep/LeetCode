# 输入一棵二叉树的根节点，判断该树是不是一棵平衡二叉树
# 如果二叉树中任意节点的左右子树深度相差不超过1，那么它就是一棵平衡二叉树


def isBalanced(root):
    banlance = False
    if getDepth(root):
        banlance = True
    return banlance


# 在判断左右子树是否平衡的过程中把深度计算出来
# 这样在对父结点进行平衡判断时就可以不用再重复计算左右子树的深度
# 相当于后序遍历
def getDepth(root):
    if not root:
        return 0
    left = getDepth(root.left)
    right = getDepth(root.right)
    if abs(left-right) > 1:
        return False
    return max(left, right) + 1
