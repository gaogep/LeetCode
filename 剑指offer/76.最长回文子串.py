# 给定一个字符串s，找到s中最长的回文子串，你可以假设s的最大长度为1000
# 解题思路: 双指针


def find_palindrome(s, left, right):
    # 左右双指针，然后以某个字符为中心，向两边展开
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left:right+1]


def longest_palindrome(s):
    ret = ''
    for i in range(len(s)):
        s1 = find_palindrome(s, i, i)    # 找到以s[i]为中心的最长回文子串
        s2 = find_palindrome(s, i, i+1)  # 找到以s[i+1]为中心的最长回文子串
        if len(ret) <= len(s1):
            ret = s1
        if len(ret) <= len(s2):
            ret = s2
    return ret
