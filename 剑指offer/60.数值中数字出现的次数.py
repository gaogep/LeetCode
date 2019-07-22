# 数组中只出现一次的两个数字
# 一个整型数组中除了两个数字之外，其他的数字都出现了两次
# 请找出两个只出现一次的数字，要求时间和空间复杂度分别为o(n)和o(1)


arr = [2, 3, 4, 6, 3, 2, 5, 5]


def findOnce(arr):
    if not arr:
        return
    xor = 0
    # 从头到尾异或数组中的每个数字，那么最终得到的结果
    # 就是两个只出现一次的数字的异或结果 上面的例子就是得到的就是 4 ^ 6 的结果
    for i in arr:
        xor ^= i
    num1, num2 = 0, 0
    # 由于两个数字是不同的，我们在结果数字中倒找第一个为1的位的位置记为第n位
    # 给mask在该位置设置成1，mask的其余位置是0
    # mask存在的意义在于我们能通过该位置来分辨出两个只出现了一次的数字
    mask = 1
    while xor & mask == 0:
        mask <<= 1
    for num in arr:
        # 与mask做与运算将数组中的数字区分成两类
        if num & mask == 0:
            # 然后分别与0进行异或运算
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


print(findOnce(arr))
