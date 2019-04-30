def count_recursive(arr):
    number = 0
    if arr:
        number += 1 + count_recursive(arr[1:])
    return number


my_list = [1, 3, 5, 7, 9]
print(count_recursive(my_list))
