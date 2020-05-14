class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        right = nums[-3] * nums[-2] * nums[-1]
        left = nums[0] * nums[1] * nums[-1]
        return max(left, right)
