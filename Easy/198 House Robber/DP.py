class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i] + memo[i-1], memo[i])
            
        return memo[len(nums)]
