class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            if target - num in dic and dic[target - num] != i:
                return [i, dic[target - num]]
nums = [2, 7, 11, 15]
target = 9
p = Solution()
print(p.twoSum(nums,target))