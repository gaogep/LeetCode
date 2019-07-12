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

    temp = root.left
    root.left = root.right
    root.right = temp

    if root.left:
        showMirror(root.left)
    if root.right:
        showMirror(root.right)


def showMirrorLoop(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        node.left, node.right = node.right, node.left


showMirrorLoop(root)
print(root.value)
print(root.left.value, " ", end="")
print(root.right.value)
print(root.left.left.value, " ", end="")
print(root.right.right.value)
