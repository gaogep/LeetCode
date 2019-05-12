from random import shuffle

my_list = [i for i in range(50)]
shuffle(my_list)


def divide(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(divide(arr[:mid]), divide(arr[mid:]))


def merge(arr1, arr2):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    result += arr1
    result += arr2
    return result


def MergeSort(arr):
    return divide(arr)


print(MergeSort(my_list))
