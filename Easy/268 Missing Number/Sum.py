class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_sum = sum(nums)
        return n * (n + 1) / 2 - num_sum
