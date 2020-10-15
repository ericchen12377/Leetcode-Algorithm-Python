class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or x > 2**31 - 1 or (x % 10 == 0 and x != 0):
            return False
        else:
            res = 0
            while x > res:
                res = 10 * res + (x % 10)
                x = x // 10
            return res == x or x == res // 10





x =  121
p = Solution()
print(p.isPalindrome(x))