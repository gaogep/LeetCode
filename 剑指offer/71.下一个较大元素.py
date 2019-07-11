# 现在我们有一个int数组，请你找出数组中每个元素的下一个比它大的元素
# 给定一个int数组A及数组的大小n，请返回一个int数组,代表每个元素比他
# 大的下一个元素,若不存在则为-1。保证数组中元素均为正整数


arr = [11, 13, 10, 5, 12, 21, 3]


def findNextLarger(arr, n):
    result = []
    stack = [-1]
    for i in range(n-1, -1, -1):
        while arr[i] > stack[len(stack)-1] and stack[len(stack)-1] != -1:
            stack.pop()
        result.append(stack[len(stack)-1])
        stack.append(arr[i])
    return list(reversed(result))


print(findNextLarger(arr, 7))
