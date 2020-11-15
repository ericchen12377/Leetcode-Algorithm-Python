class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        nums = [-float('inf')] + nums + [-float('inf')]
        for i in range(1, len(nums) - 1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i - 1

        return -1