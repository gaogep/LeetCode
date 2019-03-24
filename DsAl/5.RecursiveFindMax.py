def findmax_recursive(arr):
    if arr:
        max_num = max(arr[0], findmax_recursive(arr[1:]))
    else:
        max_num = -1
    return max_num

print(findmax_recursive([1, 2, 3, 4, 5]))