# 输入一个正数s,打印出所有和为s的连续正数序列(至少含有两个数)
# 例如，输入15,由于1+2+3+4+5=4+5+6=7+8=15,所以打印出3个连续序列
# 1-5 4-6 7-8


def printSerialSeq(number):
    if number < 3:
        return

    start, end = 1, 2
    stop = (1 + number) // 2
    curSum = start + end

    while start < stop:
        if curSum == number:
            printSeq(start, end)
        while curSum > number and start < stop:
            curSum -= start
            start += 1
            if curSum == number:
                printSeq(start, end)
        end += 1
        curSum += end


def printSeq(start, end):
    print([i for i in range(start, end+1)])


printSerialSeq(15)
