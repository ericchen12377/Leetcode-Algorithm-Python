class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)[2:]
        return all(bin_n[i] != bin_n[i+1] for i in range(len(bin_n) - 1))
n = 5
p = Solution()
print(p.hasAlternatingBits(n))