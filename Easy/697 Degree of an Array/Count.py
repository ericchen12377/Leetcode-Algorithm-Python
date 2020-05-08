import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return 1
        degree = max([nums.count(num) for num in nums_set])
        most_numbers = [num for num in nums_set if nums.count(num) == degree]
        scale = 100000000
        for most_number in most_numbers:
            appear = [i for i,num in enumerate(nums) if num == most_number]
            appear_scale = max(appear) - min(appear) + 1
            if appear_scale < scale:
                scale = appear_scale
        return scale
nums = [1,2,2,3,1,4,2]
p = Solution()
print(p.findShortestSubArray(nums))