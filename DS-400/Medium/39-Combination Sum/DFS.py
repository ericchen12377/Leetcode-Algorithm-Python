class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        self.DFS(candidates, target, [], res)
        return res
        
    def DFS(self, candidates, target, out, res):
        if target < 0:
            return
        if target == 0:
            res.append(out)
            return
        for i in range(len(candidates)):
            self.DFS(candidates[i:], target - candidates[i], out + [candidates[i]], res)