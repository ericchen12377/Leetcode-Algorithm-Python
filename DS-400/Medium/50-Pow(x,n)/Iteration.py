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
        res = 1
        cur_res = x
        if n == 0:
            return res
        i = n
        while i > 0:
            if i % 2 == 1:
                res = res * cur_res
            i = i / 2
            cur_res = cur_res * cur_res
        return res