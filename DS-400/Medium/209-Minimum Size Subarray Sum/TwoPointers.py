class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        
        """
        if not nums:
            return 0
        val, res, left = 0, float('inf'), 0
        for right in range(0, len(nums)):
            val += nums[right]
            while val >= s:
                res = min(res, right - left + 1)
                val -= nums[left]
                left += 1
                
        return 0 if res == float('inf') else res