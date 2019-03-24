my_list = [8, 5, 63, 21, 19, 1, 76, 2, 9, 18, 33]


def insertion(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        index = i
        while index > 0 and arr[index-1] > tmp:
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = tmp
    return arr

print(insertion(my_list))
