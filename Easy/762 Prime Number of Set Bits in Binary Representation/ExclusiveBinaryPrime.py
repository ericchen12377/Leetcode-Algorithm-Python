class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] #at most 32 for binary number
        res = 0
        for num in range(L, R + 1):
            if bin(num).count("1") in primes:
                res += 1
        return res
L = 6
R = 10
p = Solution()
print(p.countPrimeSetBits(L,R))