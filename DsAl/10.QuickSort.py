arr = [8, 5, 63, 21, 19, 1, 76, 2, 9, 18, 33]


def getPivot(arr):
    high = len(arr) - 1
    low = 0
    center = int((high + low) / 2)
    if arr[low] > arr[center]:
        arr[low], arr[center] = arr[center], arr[low]
    if arr[center] > arr[high]:
        arr[center], arr[high] = arr[high], arr[center]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    return arr[center]


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = getPivot(arr)
    pivot = arr[0]
    arr.remove(pivot)
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
