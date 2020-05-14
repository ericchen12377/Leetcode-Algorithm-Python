class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        while n >= i:
            res += n / i
            i *= 5
        return res
