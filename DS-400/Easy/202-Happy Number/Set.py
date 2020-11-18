class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def getn(n):
            res = 0
            while n:
                res += (n % 10)**2
                n = n // 10
            return res
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getn(n)          
        return n == 1