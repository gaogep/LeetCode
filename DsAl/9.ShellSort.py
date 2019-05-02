from random import shuffle

my_list = [i for i in range(100)]
shuffle(my_list)


def insertion(arr, gap):
    for i in range(gap, len(arr)):
        tmp = arr[i]
        index = i
        while index > 0 and arr[index-gap] > tmp:
            arr[index] = arr[index-gap]
            index -= gap
        arr[index] = tmp
    return arr


def shell(arr):
    seq = [929, 505, 209, 109, 41, 19, 5, 1]
    _seq = filter(lambda x: x < len(arr), seq)
    for gap in _seq:
        arr = insertion(arr, gap)
    return arr


# print(insertion(my_list, 1))
print(shell(my_list))
