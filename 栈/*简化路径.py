# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = []
        segments = path.split("/")
        for segment in segments:
            path_stack.append(segment)
            if segment == "." or segment == '':
                path_stack.pop()
            elif segment == "..":
                if len(path_stack) > 1:
                    path_stack.pop()
                    path_stack.pop()
                else:
                    path_stack.pop()

        ans = "/".join(path_stack)
        if not ans.startswith("/"):
            ans = "/" + ans
        # print "ans:", ans
        return ans
