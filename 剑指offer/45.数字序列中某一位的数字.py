# 数字以012345678910111213141516....的格式序列化到
# 一个字符序列中.在这个序列中,第5为(从0开始计数)是5
# 第19位是4,等等.请写一个函数,求任意n为对应的数字


def findNumber(index):
    if index < 0:
        return
    digits = 1
    while True:
        numbers = cntofIntergers(digits)
        if index < numbers * digits:
            return digitAtindex(index, digits)
        index -= digits * numbers  # 跳过digits * numbers位数
        digits += 1


def cntofIntergers(digits):
    """计算m位的数字总共有多少个"""
    if digits == 1:
        return 10
    return 9 * (10**(digits-1))


def beginNumber(digits):
    """m位数的起始数字"""
    if digits == 1:
        return 0
    return 10**(digits-1)


def digitAtindex(index, digits):
    number = beginNumber(digits) + index // digits  # 得到包含index的数字
    indexright = digits - index % digits            # 计算偏移量
    for i in range(1, indexright):
        number /= 10
    return number % 10
