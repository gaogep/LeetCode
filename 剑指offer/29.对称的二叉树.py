# 请实现一个函数,用来判断一棵二叉树是不是对称的.
# 如果一棵二叉树和它的镜像一样,那么它是对称的.


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isSymmetrical(root1, root2):
    if not root1 and not root2:
        return True

    if not (root1 and root2):
        return False

    if root1.value != root2.value:
        return False
    # 左右相等 右左相等 即为对称
    return isSymmetrical(root1.left, root2.right) \
        and isSymmetrical(root1.right, root2.left)


def Symmetrical(root):
    return isSymmetrical(root, root)
