# 输入一棵二叉搜索树,将该二叉搜索树转换成一个排序的双向链表
# 要求不能创建任何新节点，只能调整树中节点的位置．


class bsTreeNote:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, root, value):
        if not root:
            root = bsTreeNote(value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        return root


root = bsTreeNote(10)
root.insert(root, 6)
root.insert(root, 14)
root.insert(root, 4)
root.insert(root, 8)
root.insert(root, 12)
root.insert(root, 16)


class Solution:
    def Convert(self, pRootOfTree):
        self.linkedlistLast = None
        self.convertNode(pRootOfTree)
        pHead = self.linkedlistLast
        while pHead and pHead.left:
            pHead = pHead.left
        return pHead

    def convertNode(self, root):
        if not root:
            return
        pcurr = root
        if pcurr.left:
            self.convertNode(pcurr.left)
        pcurr.left = self.linkedlistLast
        if self.linkedlistLast:
            self.linkedlistLast.right = pcurr
        self.linkedlistLast = pcurr
        if pcurr.right:
            self.convertNode(pcurr.right)


h = Solution().Convert(root)
