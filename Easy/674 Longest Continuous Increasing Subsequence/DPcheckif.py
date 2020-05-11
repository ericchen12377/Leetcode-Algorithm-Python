class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        dp = 1
        res = 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                dp += 1
                res = max(res, dp)
            else:
                dp = 1
        return res
