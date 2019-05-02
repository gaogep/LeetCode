from random import shuffle

my_list = [i for i in range(30)]
shuffle(my_list)
print(my_list)


def bucketsort(arr):
    max_val = max(arr)
    bucket = [0 for i in range(max_val+1)]
    for val in arr:
        bucket[val] = 1
    return [i for i in range(max_val+1) if bucket[i]]


print(bucketsort(my_list))
