class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N <= 1: return N
        left, right = 0, 1
        while right < N:
            while right < N and nums[right] == nums[left]:
                right += 1
            left += 1
            if right < N:
                nums[left] = nums[right]
        return left
