# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长
# 子字符串的长度。假设字符创中只包含a-z的字符
# 例如在字符串中arabcacfr 最长不含重复字符的子字符串是 acfr

strs = 'arabcacfr'

# 利用动态规划,定义f(i)为第i个字符为结尾的不包含重复字符的子字符串的最长长度
# 如果第i个字符之前没有出现过，那么f(i) = f(i-1)+1
# 如果第i个字符之前已经出现过,先计算第i个字符和它上次出现在字符串中的位置的距离d
# 然后分两种情况进行分析
# 1.d <= f(i-1) =>  d = f(i)
# 2.d > f(i-1) =>   d = f(i-1) + 1


# 方法1
def findsubstring1(s):
    pass


# -------------------------------


# 方法2
def findsubstring2(s):
    res = 0
    u = ''
    for i in range(len(s)):
        t = s[i]
        if t not in u:
            u += t
            res = max(len(u), res)
        else:
            index = u.find(t)
            u = u[index+1:]+t
    return res


print(findsubstring2(strs))
