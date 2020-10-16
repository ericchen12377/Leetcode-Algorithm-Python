class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if not digits:
            return []
        
        res = []
        def dfs(res, index, path):
            if len(path)==len(digits):
                res.append(path)
                return None
            else:
                for c in dicts[digits[index]]:
                    print(index + 1)
                    dfs(res, index+1, path + c)
        dfs(res, 0, "")
        return res



digits = "23"
p = Solution()
print(p.letterCombinations(digits))