class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        self.res = []
        self.backtrack(nums, [], 0)
        return self.res
    
    def backtrack(self, nums, current, start):
        self.res.append(current)
        if start > len(nums):
            return
        for i in range(start, len(nums)):
            if i > start and nums[i-1] == nums[i]:
                continue
            self.backtrack(nums, current + [nums[i]], i + 1)