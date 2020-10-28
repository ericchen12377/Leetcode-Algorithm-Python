from math import e, log
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        res = x
        while res * res > x:
            res = (res + x // res) // 2
        return res