class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or x > 2**31 - 1:
            return False
        else:
            res = 0
            x_org = x
            while x != 0:
                res = 10 * res + (x % 10)
                x = x // 10
            return res == x_org





x =  121
p = Solution()
print(p.isPalindrome(x))