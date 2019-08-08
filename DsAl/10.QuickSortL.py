def partition(arr, low, high):
    i = low - 1  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quickSort(arr):
    low = 0
    high = len(arr-1)
    pi = partition(arr, low, high)
    partition(arr, low, pi-1)
    partition(arr, pi-1, high)
