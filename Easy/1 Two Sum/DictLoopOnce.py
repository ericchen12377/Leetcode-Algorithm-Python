class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        pos = dict()
        for i, num in enumerate(nums):
            if target - num in pos:
                return [pos[target - num], i]
            else:
                pos[num] = i
        return [0, 0]
nums = [2, 7, 11, 15]
target = 9
p = Solution()
print(p.twoSum(nums,target))