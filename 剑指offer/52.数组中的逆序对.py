# 在数组中的两个数组，若前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对，输入一个数组，求出这个书中的逆序对的总数
# 例如在数组[7, 5, 6, 4]中，一共存在5个逆序对, 分别是
# (7, 6) (7, 5) (7, 4) (6, 4) (5, 4)


arr = [7, 5, 6, 4]
cnt = 0


# 利用归并排序 从逆序对的概念入手
# 一个在前的元素大于一个在后的元素即可组成逆序对 而一个排序好的数组逆序对数为0
# 所以从排序角度来看，我们只要将每一个逆序对转换为正序，最后数组则是有序的
# 在转换为正序的过程中正好可以统计逆序对的数量
def findReversePairs(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return count(findReversePairs(arr[:mid]), findReversePairs(arr[mid:]))


def count(arr1, arr2):
    global cnt
    res = []
    while arr1 and arr2:
        # 若第一个数组中第一个元素大于第二个数组中第一个元素
        # 而这两个数组又是排好序的 那么说明逆序对的数量为第一个数组的长度
        if arr1[0] > arr2[0]:
            res.append(arr2.pop(0))
            cnt += len(arr1)
        else:
            res.append(arr1.pop(0))
    res += arr1
    res += arr2
    return res


def findReversePairs2(arr):
    cnt = 0
    sorted_arr = sorted(arr)
    print(sorted_arr)
    for num in sorted_arr:
        cnt += arr.index(num)
    return cnt


findReversePairs(arr)
print(cnt)
