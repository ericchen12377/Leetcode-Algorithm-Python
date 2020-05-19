class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        while num * num > x:
            num = (num + x / num) / 2
        return num
