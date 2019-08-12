#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


class Solution:
    def reverse(self, x: int) -> int:
        digit_list = []
        if not x:
            return x
        elif x < 0:
            digit_list.append('-')
            x *= -1

        # 把数字后面的0全删掉
        while x % 10 == 0:
            x = x // 10

        while x != 0:
            digit_list.append(str(x % 10))
            x = x // 10

        reverse_num = int(''.join(digit_list))
        if reverse_num > 2147483647 or reverse_num < -2147483648:
            return 0

        return reverse_num

# print(Solution().reverse(1534236469))
