class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n ^= (n >> 1)
        return not (n & n + 1)
n = 5
p = Solution()
print(p.hasAlternatingBits(n))
n = 7
p = Solution()
print(p.hasAlternatingBits(n))