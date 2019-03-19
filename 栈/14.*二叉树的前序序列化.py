class Solution(object):
    # 空节点的数量 = 非空节点的数量 + 1
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        res = 1
        for val in preorder.split(','):
            if not res:
                return False
            if val == "#":
                res -= 1
            else:
                res += 1
        return not res

# "9,3,4,#,#,1,#,#,2,#,6,#,#"