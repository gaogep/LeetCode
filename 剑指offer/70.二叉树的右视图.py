class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


def rightView(root):
    if not root:
        return
    queue = [[root]]
    while queue:
        level = []
        tmp_list = queue.pop(0)
        for i in range(len(tmp_list)):
            if tmp_list[i].left:
                level.append(tmp_list[i].left)
            if tmp_list[i].right:
                level.append(tmp_list[i].right)
            if i == len(tmp_list) - 1:
                print(tmp_list[i].val)
        if level:
            queue.append(level)


rightView(root)
