class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        res = 0
        for i in range(N):
            c1, c0 = 0, 0
            if s[i] == "1":
                c1 = 1
            else:
                c0 = 1
            for j in range(i + 1, N):
                if s[j] == "1":
                    c1 += 1
                else:
                    c0 += 1
                if c0 == c1:
                    res += 1
                    break
        return res
p = Solution()
S = "00110011"
print(p.countBinarySubstrings(S))