class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1 << 32
        res = 0
        while mask:
            if n & mask:
                res += 1
            mask >>= 1
        return res
