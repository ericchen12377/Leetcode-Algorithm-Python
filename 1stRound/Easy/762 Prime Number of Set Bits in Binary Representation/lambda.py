class Solution(object):
    def countPrimeSetBits(self, L, R):
        isPrime = lambda num : 0 if ((num == 1) or (num % 2 == 0 and num > 2)) else int(all(num % i for i in range(3, int(num ** 0.5) + 1, 2)))
        return sum(isPrime(bin(num)[2:].count('1')) for num in range(L, R+1))
L = 6
R = 10
p = Solution()
print(p.countPrimeSetBits(L,R))