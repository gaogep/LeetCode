# 输入一颗二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点
# 形成的一条路径，最长路径的长度为树的深度


# 递归实现：二叉树的最大深度为左右子树的最大深度加1
def getTreeDepth(root):
    if not root:
        return 0
    left = getTreeDepth(root.left)
    right = getTreeDepth(root.right)
    return max(left, right) + 1


# 循环实现: 层序遍历
def getTreeDepthLevel(root):
    if not root:
        return
    depth = 0
    nodelist = [root]
    while nodelist:
        tmplist = []
        for node in nodelist:
            if node.left:
                tmplist.append(node.left)
            if node.right:
                tmplist.append(node.right)
        nodelist = tmplist
        depth += 1
    return depth
