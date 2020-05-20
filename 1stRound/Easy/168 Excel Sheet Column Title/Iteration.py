class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return 'A'
        res = ""
        while n:
            if n % 26 == 0:
                res = "Z" + res
                n -= 26
            else:
                res = chr(ord('A') - 1 + n % 26) + res
                n -= n % 26
            n /= 26
        return res
