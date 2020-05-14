class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cur = 0, 0
        for value in nums:
            prev, cur = cur, max(prev + value, cur)
        return cur
