class Treeroot(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        que = []

        if root:
            que.append(root)
            res.append([root.val])

        flg = 1
        while que:
            i = 0
            length = len(que)
            tmp_list = []
            while i < length:
                tmp = que.pop(0)
                if tmp.left:
                    que.append(tmp.left)
                    tmp_list.append(tmp.left.val)
                if tmp.right:
                    que.append(tmp.right)
                    tmp_list.append(tmp.right.val)
                i += 1
            if tmp_list and flg == 1:
                res.append(tmp_list[::-1])
            elif tmp_list and flg == -1:
                res.append(tmp_list)
            flg *= -1
        return res
