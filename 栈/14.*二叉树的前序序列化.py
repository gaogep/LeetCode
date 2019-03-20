class Solution(object):
    # 叶节点数目比非叶节点多1，并且不到最后，res不能<=0
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