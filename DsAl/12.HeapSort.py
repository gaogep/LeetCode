from random import shuffle

my_list = [i for i in range(100)]
shuffle(my_list)
print(my_list)


def adjust(arr, root, rest):
    init_val = arr[root]
    parent = root
    while parent * 2 + 1 < rest:
        child = parent * 2 + 1
        if child != rest - 1 and arr[child+1] > arr[child]:
            child += 1
        if init_val > arr[child]:
            break
        else:
            arr[parent] = arr[child]
            parent = child
    arr[parent] = init_val


def heapsort(arr):
    length = len(arr)
    for i in range(length//2-1, -1, -1):
        adjust(arr, i, length)
    for i in range(length-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust(arr, 0, i)
    return arr


print(heapsort(my_list))
