class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 核心思想: 分治法
# 对于一个节点，如果在左子树找到了a，在右子树找到了b
# 那么这个节点就是 a 和 b 的公共节点
def commonAncester(root, a, b):
    if not root or root == a or root == b:
        return root

    left = commonAncester(root.left, a, b)
    right = commonAncester(root.right, a, b)

    if left and right:
        return root

    if not left:
        return right

    if not right:
        return left

    return None
