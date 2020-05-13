class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        return -1
