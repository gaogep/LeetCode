# 利用堆排序
# (1) 遍历输入数组，将前k个数插入到推中；（利用multiset来做为堆的实现）
# (2) 继续从输入数组中读入元素做为待插入整数，并将它与堆中最大值比较：
#     如果待插入的值比当前已有的最大值小，则用这个数替换当前已有的最大值；
#     如果待插入的值比当前已有的最大值还大，则抛弃这个数，继续读下一个数
#     这样动态维护堆中这k个数，以保证它只储存输入数组中的前k个最小的数，最后输出堆即可

import heapq
arr = [4, 5, 1, 6, 2, 7, 3, 8]


def find_kth_smallest(arr, k):
    res = []
    if not arr:
        return res
    for num in arr:
        if len(res) < k:
            # 构建一个只有k个元素的最大堆
            # 由于heapq实现的是最小堆
            # 所以要把每个数字取反
            heapq.heappush(res, -num)
        else:
            # 将后续元素与最大堆的堆顶比较
            # 如果该元素小于堆顶 删除堆顶元素把这个
            # 元素插入最大堆中进行调整
            heapq.heappushpop(res, -num)
    print(list(map(lambda x: -x, res)))


find_kth_smallest(arr, 4)
