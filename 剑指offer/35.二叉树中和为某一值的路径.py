# 输入一棵二叉树和一个整数,打印出二叉树中节点值的和为
# 输入整数的所有路径.从树的根节点开始往下一直到叶节点所
# 经过的节点形成一条路径


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = treeNode(10)
root.left = treeNode(5)
root.right = treeNode(12)
root.left.left = treeNode(4)
root.left.right = treeNode(7)


def findPath(root, target):
    if not root:
        return
    res = []
    dfs(root, res, [root.value], target)
    return res


def dfs(root, res, path, target):
    if not root.left and not root.right and sum(path) == target:
        res.append(path)
    if root.left:
        dfs(root.left, res, path+[root.left.value], target)
    if root.right:
        dfs(root.right, res, path+[root.right.value], target)


print(findPath(root, 22))
