def binary_serach(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > item:
            high = mid - 1
        elif arr[mid] < item:
            low = mid + 1
        else:
            return mid
    return '查找的元素不存在'


my_list = [1, 3, 5, 7, 9]
print(binary_serach(my_list, 9))
