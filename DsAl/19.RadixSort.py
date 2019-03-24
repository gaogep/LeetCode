my_list = [2, 32, 63, 7, 199, 3452, 18932, 25, 77, 90, 321, 654, 783]


def radixsort(arr, times):
    for time in range(times):
        buckets = [[] for i in range(10)]
        for num in arr:
            buckets[num//(10**time)%10].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr

# 待排序列中最大的数字为5位数->LSD法 次位优先
print(radixsort(my_list, 5))
