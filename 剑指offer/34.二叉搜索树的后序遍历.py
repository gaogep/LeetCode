# 输入一个整数数组 判断该数组是不是某二叉搜索树的后序遍历结果
# 如果是返回true 否则返回false


arr = [5, 7, 6, 9, 11, 10, 8]  # true


def isPostOrder(arr):
    if not arr:
        return False

    root = arr.pop()

    # 二叉搜索树的左子树全部小于根节点
    t = 0
    for i in range(len(arr)):
        if arr[i] > root:
            t = i
            break

    # 二叉搜索树的右子树全部大于根节点
    for j in range(t, len(arr)):
        if arr[j] < root:
            return False

    left = right = True

    # t > 0 说明含有左子树,然后递归进行判断
    if t > 0:
        left = isPostOrder(arr[:t])

    # 如果t比数组的长度还大,说明不包含右子树,否则递归进行判断
    if t < len(arr):
        right = isPostOrder(arr[t:])

    return (left and right)


print(isPostOrder(arr))
