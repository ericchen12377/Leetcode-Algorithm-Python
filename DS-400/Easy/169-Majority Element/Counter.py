class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        return list(dic.keys())[list(dic.values()).index(max(dic.values()))]