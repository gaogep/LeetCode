from random import shuffle

my_list = [i for i in range(5000)]
shuffle(my_list)
print(my_list)


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
    result = [[i] for i in arr]
    while len(result) != 1:
        result.append(merge(result.pop(0), result.pop(0)))
    return result[0]


print(MergeSort(my_list))
