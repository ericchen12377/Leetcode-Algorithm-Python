class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = 0b1010101010101010101010101010101010101010101010101010101010101010
        while b > 0:
            if b == n:
                return True
            b = b >> 1
        return False
n = 5
p = Solution()
print(p.hasAlternatingBits(n))
n = 7
p = Solution()
print(p.hasAlternatingBits(n))