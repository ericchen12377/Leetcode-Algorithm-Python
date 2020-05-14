class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        N = len(nums)
        if N == 1: return nums[0] * 1.0
        sums = [0] * (N + 1)
        for i in range(1, N + 1):
            sums[i] = nums[i - 1] + sums[i - 1]
        res = float("-inf")
        for i in range(k, N + 1):
            res = max(sums[i] - sums[i - k], res)
        return res / float(k)
