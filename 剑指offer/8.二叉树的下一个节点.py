# 给定一棵二叉树和其中的一个节点,如何找出中序遍历的下一个节点
# 树中的节点除了有两个分别只向左右子节点的指针,还有指向下一个
# 父节点的指针


class treeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findNext(tNode):
    if not tNode:
        return None
    tNext = None
    # 如果一个节点有右子树
    if tNode.right:
        tNoder = tNode.right
        while tNoder.left:
            tNoder = tNoder.left
        tNext = tNoder
    # 如果一个节点没有右子树
    elif tNode.parent:
        tCurrent = tNode
        tParent = tNode.parent
        # 如果一个节点有父节点,那么判断该节点是否是其父节点的右子节点
        # 如果是,那么沿着指向父节点的指针向上寻找,直到找到一个节点是
        # 它父节点的左子节点,那么这个节点的父节点就是下一个节点
        # 这个while循环就是判断一个节点的父节点不为空
        # 且当前节点是这个父节点的右子节点,那么继续向上遍历
        # 直到找到一个节点是它父节点的左子节点跳出循环
        while tParent and tCurrent == tParent.right:
            tCurrent = tParent
            tParent = tParent.parent
        # 如果不是 下一个节点就是其父节点
        tNext = tParent
    return tNext
