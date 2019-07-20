from random import shuffle

my_list = [i for i in range(8)]
shuffle(my_list)


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
    cnt = 0
    arrlen = len(arr)
    result = [[i] for i in arr]
    while cnt // 2 < arrlen - 1:
        result.append(merge(result[cnt], result[cnt+1]))
        cnt += 2
    print(result)
    return result[-1]


print(MergeSort(my_list))
