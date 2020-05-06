class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        nums.sort()
        return any(nums[x] - nums[x + 1] == 0 for x in range(len(nums) - 1))
