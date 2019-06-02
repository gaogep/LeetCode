# 从上到下打印一棵二叉树, 同一层的几点按从左到右的顺序打印
# 每一层打印一行.
# 1
# 2 3
# 4 5 6 7


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = treeNode(1)
root.left = treeNode(2)
root.left.left = treeNode(4)
# root.left.right = treeNode(5)
# root.right = treeNode(3)
# root.right.left = treeNode(6)
# root.right.right = treeNode(7)


def level(root):
    if root:
        queue = []
        queue.append(root)
        nextLevel = 0
        toBePrinted = 1
        while queue:
            tmp = queue.pop(0)
            print(tmp.value, ' ',  end='')
            if tmp.left:
                queue.append(tmp.left)
                nextLevel += 1
            if tmp.right:
                queue.append(tmp.right)
                nextLevel += 1
            toBePrinted -= 1
            if toBePrinted == 0:
                print('\n')
                toBePrinted = nextLevel
                nextLevel = 0


level(root)
