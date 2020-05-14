class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]
        dists = [0] * len(binary)
        left = 0
        for i, b in enumerate(binary):
            if b == '1':
                dists[i] = i - left #save each distance to the left 1
                left = i
        return max(dists) #find max
N = 5
p = Solution()
print(p.binaryGap(N))