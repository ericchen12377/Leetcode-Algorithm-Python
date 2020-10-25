class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n == 0:
            return res
        elif n > 0:
            for i in range(n):
                res = res * x
        else:
            for i in range(abs(n)):
                res = res * (1/x)
        return res