# 输入一个字符串,打印出该字符串中字符的所有排列.
# 例如输入字符串a b c
# abc acb bac bca cab cba


# 将字符串看成两部分
# 第一个字符和后面所有的字符
def Permutation(ss):
    if not ss:
        print(",")
    for i in range(len(ss)):
        print(ss[i], end="")
        # 第一个字符 + 剩余的字符
        Permutation(ss[:i]+ss[i+1:])


Permutation('abc')
