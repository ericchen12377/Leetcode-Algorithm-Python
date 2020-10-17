class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        def helper(self, left, right, out, res):
            if(left < 0 or right < 0 or left > right):
                return
            if (left == 0 and right == 0):
                res.append(out)
                return
            self.helper(left - 1, right, out + "(", res)
            self.helper(left, right - 1, out + ")", res)
        self.helper(n, n, "", res)
        return res

n = 3
p = Solution()
print(p.generateParenthesis(n))