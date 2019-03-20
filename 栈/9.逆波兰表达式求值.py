# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        symbols = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in symbols:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    c = b + a
                elif token == "-":
                    c = b - a
                elif token == "*":
                    c = b * a
                else:
                    c = int(b / a)
                stack.append(c)
        return stack.pop()

s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
