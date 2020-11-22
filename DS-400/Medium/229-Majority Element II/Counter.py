class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = collections.Counter(nums)
        return [ list(dic.keys())[j] for j in [i for i in range(len(list(dic.values()))) if list(dic.values())[i] > len(nums)/3]]