class Solution(object):
    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        nums = sorted(nums)
        while left != right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
        return [0, 0]


nums = [7, 2, 11, 15]
target = 9
p = Solution()
print(p.TwoSum(nums,target))