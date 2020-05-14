class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            if (x & 1) ^ (y & 1): #x & 1 is equivalent to x % 2, x >> 1 is equivalent to x / 2
                res += 1
            x >>= 1
            y >>= 1
        return res
x = 1
y = 4
p = Solution()
print(p.hammingDistance(x, y))