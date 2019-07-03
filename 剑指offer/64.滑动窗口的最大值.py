# 给定一个数组和滑动窗口大小，请找出所有滑动窗口里的最大值
# [[2, 3, 4], 2, 6, 2, 5, 1] 窗口大小为3


arr = [2, 3, 4, 2, 6, 2, 5, 1]


def maxInWindow(arr, size):
    # 存放可能是最大值的下标
    maxqueue = []
    # 存放窗口中最大值
    maxlist = []
    n = len(arr)
    # 参数检验
    if n == 0 or size == 0 or size > n:
        return maxlist
    for i in range(n):
        # 判断队首下标对应的元素是否已经滑出窗口
        if len(maxqueue) > 0 and i - size >= maxqueue[0]:
            maxqueue.pop(0)
        # 如果新来的元素比队列中的元素大，则将队列中的元素弹出直至剩余元素大于新来的元素
        while len(maxqueue) > 0 and arr[i] > arr[maxqueue[-1]]:
            maxqueue.pop()
        # 将元素的下标加入队列中
        maxqueue.append(i)
        # 共计进行n-1次窗口滑动 只要 i+1 >= size 就得获取一次最大值
        if i >= size - 1:
            maxlist.append(arr[maxqueue[0]])
    return maxlist


print(maxInWindow(arr, 3))
