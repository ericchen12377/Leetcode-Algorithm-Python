class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        begin = 0
        for i in range(N):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin += 1
        return begin
