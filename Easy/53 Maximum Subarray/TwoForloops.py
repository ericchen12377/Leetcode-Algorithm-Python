class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preSum = [0 for i in range(len(nums))]
        preSum[0] = nums[0]
        for i in range(len(nums)-1):
            preSum[i + 1] = preSum[i] + nums[i]
        
        res = -100000000000000
        for i in range(len(nums)):
            for j in range(len(nums)):
                 res = max(res, preSum[j] - preSum[i])
        return res