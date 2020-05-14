class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A) - min(A) - 2 * K, 0)
A = [1,3,6]
K = 3
p = Solution()
print(p.smallestRangeI(A,K))