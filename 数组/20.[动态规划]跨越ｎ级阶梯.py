# 跨越n级台阶有几种方法

# 递归
def recur_climber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return recur_climber(n-1) + recur_climber(n-2)

# 动态规划
def dp_climber(n):
    if n == 1:
        return 1
    res = [-1 for x in range(n+1)]
    res[1] = 1
    res[2] = 2
    for i in range(3, n+1):
        res[i] = res[i-1] + res[i-2]
    return res[n]

print(dp_climber(10))