import collections
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        count = collections.Counter(nums)
        return count.most_common(1)[0][1] > 1
