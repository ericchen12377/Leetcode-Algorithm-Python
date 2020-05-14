class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        l = N - 1
        res = ""
        for i, s in enumerate(S):
            if s.isalpha():
                while not S[l].isalpha():
                    l -= 1
                res += S[l]
                l -= 1
            else:
                res += s
        return res
S = "a-bC-dEf-ghIj"
p = Solution()
print(p.reverseOnlyLetters(S))