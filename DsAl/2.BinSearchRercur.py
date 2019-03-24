def bsr(arr, item):
    low = 0
    high = len(arr) - 1
    if low <= high:
        mid = int((low + high) / 2)
        if arr[mid] > item:
            mid = bsr(arr[low:high], item)
        elif arr[mid] < item:
            mid = bsr(arr[low+1:high], item)
        else:
            pass
    return mid

my_list = [1, 3, 5, 7, 9]
print(bsr(my_list, 5))