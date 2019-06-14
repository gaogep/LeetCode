arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSusequence(arr):
    now = 0
    maxSum = arr[0]
    for num in arr:
        now += num
        if now > maxSum:
            maxSum = now
        elif now < 0:
            now = 0
    return maxSum


print(maxSusequence(arr))
