class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y #exclusive or
        res = 0
        while xor:
            res += xor & 1
            xor >>= 1
        return res
x = 1
y = 4
p = Solution()
print(p.hammingDistance(x, y))