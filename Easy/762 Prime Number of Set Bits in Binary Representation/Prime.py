import math
class Solution(object):
    def isPrime(self, num):
        if num == 1:
            return 0
        elif num == 2:
            return 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return 0
        return 1
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return sum(self.isPrime(bin(num)[2:].count('1')) for num in range(L, R+1))
L = 6
R = 10
p = Solution()
print(p.countPrimeSetBits(L,R))