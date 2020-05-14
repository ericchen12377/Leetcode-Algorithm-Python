class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, 0, res, '')
        return res
    
    def dfs(self, string, index, res, path):
        if index == len(string):
            res.append(path)
            return
        else:
            if string[index].isalpha():
                self.dfs(string, index + 1, res, path + string[index].upper())
                self.dfs(string, index + 1, res, path + string[index].lower())
            else:
                self.dfs(string, index + 1, res, path + string[index])
S = "a1b2"
p = Solution()
print(p.letterCasePermutation(S))