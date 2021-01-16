class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n == 1:
            return res
        
        def dfs(n, start, path, res):
            if n == 1:
                res.append(path)
                return
            for i in range(start, int(n**0.5) + 1):
                if n % i == 0:
                    dfs(n/i, i, path + [i], res)
            dfs(1, n, path + [n], res)
            
        dfs(n, 2, [], res)
        return res[:-1]
    