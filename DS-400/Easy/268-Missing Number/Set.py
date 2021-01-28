class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        set_nums = set(nums)
        for i in range(size):
            if i not in set_nums:
                return i
        return i + 1
