class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bins = bin(n)[2:][::-1]
        rev = (bins + '0' * (32 - len(bins)))
        return int(rev, 2)
