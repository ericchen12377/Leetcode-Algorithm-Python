class Solution(object):
    def __init__(self):
        self.memo = dict()
        self.memo[0] = 1
        self.memo[1] = 1
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        steps = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = steps
        return steps
