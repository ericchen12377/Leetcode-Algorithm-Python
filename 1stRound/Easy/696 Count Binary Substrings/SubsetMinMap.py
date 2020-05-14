class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = map(len, s.replace('01','0 1').replace('10','1 0').split())
        return sum(min(i, j) for i,j in zip(s, s[1:]))
p = Solution()
S = "00110011"
print(p.countBinarySubstrings(S))