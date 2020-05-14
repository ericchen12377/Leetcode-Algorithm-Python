class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nset = set(nums)
        missing = N * (N + 1) / 2 - sum(nset)
        duplicated = sum(nums) - sum(nset)
        return [duplicated, missing]
