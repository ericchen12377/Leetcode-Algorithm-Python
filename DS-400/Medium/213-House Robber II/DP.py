class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        def robber(nums):
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
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        choice1 = nums[:n-1]
        choice2 = nums[1:]
        
        return max(robber(choice1), robber(choice2))