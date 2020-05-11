class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            while r >= 0 and nums[r] == val:
                r -= 1
            if l > r:
                break
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return l
