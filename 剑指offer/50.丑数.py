# 我们把只包含因子2, 3和5的数称为丑数
# 求从小到大排序的第1500个丑数。例如，6 8都是丑数，但14不是.
# 习惯上我们把1当做第一个丑数


# 利用空间换时间，用数组保存好之前已经找到的丑数
# 因为丑数只包含质因子2，3，5，假设我们已经有n-1个丑数，按照顺序排列，且第n-1的丑数为M。
# 那么第n个丑数一定是由这n-1个丑数分别乘以2，3，5，得到的所有大于M的结果中，最小的那个数


# 事实上我们不需要每次都计算前面所有丑数乘以2，3，5的结果，然后再比较大小。
# 因为在已存在的丑数中，一定存在某个数T2，在它之前的所有数乘以2都小于已有丑数，
# 而T2×2的结果一定大于M，同理，也存在这样的数T3，T5.我们只需要标记这三个数即可


def GetUglyNumber(index):
    if index < 1:
        return 0
    res = [1]
    t2, t3, t5 = 0, 0, 0
    while len(res) < index:
        minNum = (min(res[t2]*2, res[t3]*3, res[t5]*5))
        if minNum > res[-1]:
            res.append(minNum)
        # 判断加入数组的丑数是乘以 2 3 还是5得到的
        if (res[-1] == res[t2]*2):
            t2 += 1
        elif (res[-1] == res[t3]*3):
            t3 += 1
        else:
            t5 += 1
    return res[-1]


print(GetUglyNumber(1500))
