class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        N = len(s)
        res = ""
        pos = 0
        while pos < N:
            nx = s[pos : pos + k]
            res = res + nx[::-1] + s[pos + k : pos + 2 * k]
            pos += 2 * k
        return res
