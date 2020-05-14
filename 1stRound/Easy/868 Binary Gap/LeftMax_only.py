class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        nbins = bin(N)[2:]
        index = -1
        res = 0
        for i, b in enumerate(nbins):
            if b == "1":
                if index != -1:
                    res = max(res, i - index)
                index = i
        return res
N = 5
p = Solution()
print(p.binaryGap(N))