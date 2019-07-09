# 自底向上进行计算
# 根据f(0)和f(1)算出f(2)
# 后续同理


def fib(n):
    res = [0, 1]
    if n < 2:
        return res[n]
    a, b = 0, 1
    for i in range(2, n+1):
        s = a + b  # f(2) = f(0) + f(1)
        a = b      # f(0) = f(1)
        b = s      # f(1) = f(2)
    return s


for x in range(10):
    print(fib(x))
