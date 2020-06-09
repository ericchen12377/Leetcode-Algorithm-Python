class Solution(object):
    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return [0, 0]

nums = [7, 2, 11, 15]
target = 9
p = Solution()
print(p.TwoSum(nums,target))