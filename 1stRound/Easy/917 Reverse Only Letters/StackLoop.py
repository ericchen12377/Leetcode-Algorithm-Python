class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = []
        N = len(S)
        for i, s in enumerate(S):
            if s.isalpha():
                letters.append(s)
        res = ""
        for i, s in enumerate(S):
            if s.isalpha():
                res += letters.pop()
            else:
                res += s
        return res
S = "a-bC-dEf-ghIj"
p = Solution()
print(p.reverseOnlyLetters(S))