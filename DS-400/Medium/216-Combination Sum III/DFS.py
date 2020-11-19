class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def DFS(k, n, level, out, res):
            if n < 0:
                return
            if n == 0 and len(out) == k:
                res.append(out[:])
            for i in range(level, 10):
                out.append(i)
                DFS(k, n - i, i + 1, out, res)
                out.pop()
        
        res = []
        out = []
        DFS(k, n, 1, out, res)
        return res