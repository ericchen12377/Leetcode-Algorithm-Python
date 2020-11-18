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
        
        slow = n
        fast = getn(n)
        while fast != 1 and slow != fast:
            slow = getn(slow)
            fast = getn(getn(fast))          
        return fast == 1