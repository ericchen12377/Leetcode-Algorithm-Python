class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        return list(dic.keys())[list(dic.values()).index(1)]