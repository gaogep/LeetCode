from random import shuffle

my_list = [i for i in range(50)]
shuffle(my_list)

def MergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = int(len(arr)/2)
    return merge(MergeSort(arr[:mid]), MergeSort(arr[mid:]))

def merge(arr1, arr2):
    result = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    result += arr1
    result += arr2
    return result

print(MergeSort(my_list))