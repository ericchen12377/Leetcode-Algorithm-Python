class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if n == k:
            return [[i for i in range(1, n+1)]]
        return [i + [n] for i in self.combine(n-1,k-1)] + [i for i in self.combine(n-1, k)]