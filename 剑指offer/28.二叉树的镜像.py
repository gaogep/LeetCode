# 请完成一个函数,输入一棵二叉树,改函数输出它的镜像


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.right.right = treeNode(5)


def showMirror(root):
    if not root:
        return
    if not root.left and not root.right:
        return

    root.left, root.right = root.right, root.left
    if root.left:
        showMirror(root.left)
    if root.right:
        showMirror(root.right)
    return root


def showMirrorLoop(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        node.left, node.right = node.right, node.left
    return root


showMirrorLoop(root)
print(root.value)
print(root.left.value, " ", end="")
print(root.right.value)
print(root.left.left.value, " ", end="")
print(root.right.right.value)
