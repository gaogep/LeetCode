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
root.left.right = treeNode(5)
root.right = treeNode(3)
root.right.left = treeNode(6)
root.right.right = treeNode(7)


def print_level(root):
    queue = [[root]]
    while queue:
        nex_level = []
        cur_level = queue.pop(0)
        for node in cur_level:
            print(node.value, ' ', end="")
            if node.left:
                nex_level.append(node.left)
            if node.right:
                nex_level.append(node.right)
        if nex_level:
            queue.append(nex_level)
            print("\n")
        else:
            pass


print_level(root)
