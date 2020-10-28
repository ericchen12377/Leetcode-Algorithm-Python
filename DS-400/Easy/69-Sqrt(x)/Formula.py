from math import e, log
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
        