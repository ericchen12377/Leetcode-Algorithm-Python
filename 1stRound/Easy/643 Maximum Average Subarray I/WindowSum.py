class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        su = 0
        largest = float('-inf')
        for i,num in enumerate(nums):
            su += num
            if i >= k:
                su -= nums[i - k]
            if i >= k - 1:
                largest = max(su, largest)
        return float(largest) / k
