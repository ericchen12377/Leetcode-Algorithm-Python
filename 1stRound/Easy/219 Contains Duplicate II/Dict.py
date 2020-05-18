class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True
            d[num] = i
        return False
