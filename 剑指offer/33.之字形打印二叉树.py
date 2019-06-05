# 请实现一个函数按照之字形顺序打印二叉树
# 即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印,以此类推.


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


def zigzagPrint(root):
    if root:
        stack1 = [root]
        stack2 = []
        while stack1 or stack2:
            while stack1:
                node = stack1.pop()
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                print(node.value, ' ', end='')
            if stack1 or stack2:
                print('\n')

            while stack2:
                node = stack2.pop()
                if node.left:
                    stack1.append(node.right)
                if node.right:
                    stack1.append(node.left)
                print(node.value, ' ', end='')
            if stack1 or stack2:
                print('\n')


zigzagPrint(root)
