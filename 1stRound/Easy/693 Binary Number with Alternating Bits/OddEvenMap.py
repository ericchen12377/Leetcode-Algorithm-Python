class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)[2:]
        return sum(list(map(int, bin_n))[::2])==0 or sum(list(map(int, bin_n))[1::2]) == 0
n = 5
p = Solution()
print(p.hasAlternatingBits(n))
n = 7
p = Solution()
print(p.hasAlternatingBits(n))