class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if sorted(path) not in res:
            res.append(sorted(path))
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], res)