class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
        def getn(n):
            res = 0
            while n:
                res += (n % 10)**2
                n = n // 10
            return res
        
        while n != 1 and n not in cycle_members:
            n = getn(n)
        return n == 1