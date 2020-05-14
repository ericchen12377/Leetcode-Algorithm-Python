class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} #dictionary
        res = roman[s[-1]]
        N = len(s)
        for i in range(N - 2, -1, -1): #backward
            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
s = "LVIII"
p = Solution()
print(p.romanToInt(s))