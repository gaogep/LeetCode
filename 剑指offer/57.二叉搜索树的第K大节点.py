# 给定一颗二叉搜索树，请找出其中第Kda的节点


def findK(root, k):
    if not root:
        return
    stack = []
    res = []
    while root or stack:
        while root:
            root = root.left
            stack.append(root)
        if stack:
            tmp = stack.pop()
            res.append(tmp.value)
            root = tmp.right
    return res[k]
