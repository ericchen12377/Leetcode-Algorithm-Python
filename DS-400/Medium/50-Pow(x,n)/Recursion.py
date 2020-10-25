class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n < 0): 
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        half = self.myPow(x, n // 2)
        if(n % 2 == 0):
            return half * half
        else:
            return half * half * x