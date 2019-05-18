# 给你一根长度为n的绳子,请把绳子剪成m段,每段绳子的长度(n > 1 m > 1)
# 记为k[0] k[1] ... k[m] 请问k[0] * k[1] * ... k[m]
# 可能的最大乘积是多少?


def cut_dp(length):
    """
    关于 products 的解释
    在剪绳子这个题目中，由于必须要剪一刀，因此会导致当所给的绳子长度是小于4的时候，剪完之后的长度
    小于剪之前的长度。但是我们在递推的时候，例如求f(5) = max{f(1)*f(4), f(2)*f(3)} = 6
    如果令f(3)=2的话，将导致递推公式错误，因此，对于小于4的输入，我们特殊处理。
    """
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    products = [0 for i in range(length+1)]
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    # 从f(4)开始计算
    for i in range(4, length+1):
        max_val = 0
        for j in range(1, i//2+1):
            tmp = products[j] * products[i-j]
            if tmp > max_val:
                max_val = tmp
            products[i] = max_val

    print(products)
    return products[-1]
