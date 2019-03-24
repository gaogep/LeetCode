def sum_recursive(arr):
    sum = 0
    if arr:
        sum += arr[0] + sum_recursive(arr[1:])
    return sum

print(sum_recursive([1, 2, 3]))