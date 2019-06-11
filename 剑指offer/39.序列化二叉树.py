# 请事先两个函数,分别用来序列化和反序列化二叉树


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialize(root, seq):
    if not root:
        return
    seq.append(root.value)
    serialize(root.left, seq)
    serialize(root.right, seq)


def deserialize(seq):
    if not seq:
        return
    value = seq.pop(0)
    root = None
    if value != '#':
        root = treeNode(value)
        root.left = deserialize(seq)
        root.right = deserialize(seq)
    return root
