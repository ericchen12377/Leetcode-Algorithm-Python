class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2]) #get nums in odds position
input = [1,4,3,2]
p = Solution()
print(p.arrayPairSum(input))