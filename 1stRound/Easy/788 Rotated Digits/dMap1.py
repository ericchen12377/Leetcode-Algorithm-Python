class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dmap = {"0" : "0", "1" : "1", "8" : "8", "2" : "5", "5" : "2", "6" : "9", "9" : "6"}
        res = 0
        for num in range(1, N + 1):
            if any(x in str(num) for x in ["3", "4", "7"]):
                continue
            if any(x in str(num) for x in ["2", "5", "6", "9"]):
                res += 1
        return res
