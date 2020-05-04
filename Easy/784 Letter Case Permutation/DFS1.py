class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, res, "")
        return res
    
    def dfs(self, S, res, word):
        if not S:
            res.append(word)
            return
        if S[0].isalpha():
            self.dfs(S[1:], res, word + S[0].upper())
            self.dfs(S[1:], res, word + S[0].lower())
        else:
            self.dfs(S[1:], res, word + S[0])
S = "a1b2"
p = Solution()
print(p.letterCasePermutation(S))