class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pos = 0
        while pos < len(bits) - 1:
            if bits[pos] == 1:
                pos += 2
            else:
                pos += 1
        return pos == len(bits) - 1 and bits[pos] == 0
