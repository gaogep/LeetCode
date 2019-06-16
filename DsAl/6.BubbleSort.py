my_list = [8, 5, 63, 21, 19, 1, 76, 2, 9, 18, 33]


def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble(my_list))
