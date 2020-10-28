class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * (n + 1)
        return self.climb(0, n, memo)
        # i is current step
    def climb(self, i, n, memo):
        if i > n:
            return 0
        elif i == n:
            return 1
        elif memo[i] > 0:
            return memo[i]
        memo[i] = self.climb(i + 1, n, memo) + self.climb(i + 2, n, memo)
        return memo[i]