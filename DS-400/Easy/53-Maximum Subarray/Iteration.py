class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = -2147483647
        curSum = 0
        for num in nums:
            curSum = max(curSum + num, num)
            res = max(res, curSum)
        return res
        