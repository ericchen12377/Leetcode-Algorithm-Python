class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = 1
        denom = 1
        if m > n:
            small = n
        else:
            small = m
        for i in range(1, small):
            num = num * (m + n - 1 - i)
            denom*= i
        return num // denom