class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums).values()
        return sum(dic) > len(dic)