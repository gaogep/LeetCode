# 对于一个元素各不相同且按升序排列的有序序列，请编写一个算法，创建一棵高度最小的二叉查找树。
# 给定一个有序序列int[] vals,请返回创建的二叉查找树的高度


class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createMinmalBst(arr):
    if not arr:
        return
    mid = len(arr) // 2
    root = treeNode(arr[mid])
    root.left = createMinmalBst(arr[:mid])
    root.right = createMinmalBst(arr[mid+1:])
    return root
