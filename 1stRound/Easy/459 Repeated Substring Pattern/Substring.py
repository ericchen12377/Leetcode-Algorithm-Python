class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        for i in range(1, len_s // 2 + 1): #at least two substrings
            if len_s % i == 0:
                sub_s = s[:i]
                if sub_s * (len_s // i) == s:
                    return True
        return False
s = "aba"
p = Solution()
print(p.repeatedSubstringPattern(s))