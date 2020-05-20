class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len, _nums = len(nums), sorted(nums)
        if nums == _nums:
            return 0
        l = min([i for i in range(_len) if nums[i] != _nums[i]])
        r = max([i for i in range(_len) if nums[i] != _nums[i]])
        return r - l + 1
