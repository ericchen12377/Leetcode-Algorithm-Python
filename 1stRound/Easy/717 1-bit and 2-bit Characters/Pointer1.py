class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pos = 0
        while pos < len(bits) - 1:
            pos += 2 if bits[pos] == 1 else 1
        return pos == len(bits) - 1
