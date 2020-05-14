class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1') # find different bits and count 
x = 1
y = 4
p = Solution()
print(p.hammingDistance(x, y))