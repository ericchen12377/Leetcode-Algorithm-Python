class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 0
        n = len(nums)
        i = 0
        cur = 0
        while(cur < n - 1):
            res += 1
            pre = cur
            while i <= pre:
                cur = max(cur, i + nums[i])
                i += 1
            if pre == cur:
                return False
        return True