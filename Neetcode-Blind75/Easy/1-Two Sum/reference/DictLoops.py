class Solution(object):
    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = dict()
        for i, num in enumerate(nums):
            if target - num in pos:
                return [pos[target - num], i]
            else:
                pos[num] = i
        return [0, 0]


nums = [7, 2, 11, 15]
target = 9
p = Solution()
print(p.TwoSum(nums,target))