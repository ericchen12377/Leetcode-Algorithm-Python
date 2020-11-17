class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for x in range(2, len(nums)):
            dp[x] = max(dp[x - 1], nums[x] + dp[x - 2])
        
        return dp[-1]



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax,currMax = 0, 0
        for x in nums:
            tmp = currMax
            currMax = max(prevMax + x, currMax)
            prevMax = tmp
        return currMax