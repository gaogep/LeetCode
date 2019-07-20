# 给定一棵二叉 <<搜索树>>，请找出其中第K大的节点


# 直接中序遍历
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
