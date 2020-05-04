class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = 0
        for j in range(N):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

nums = [0,1,0,3,12]
p = Solution()
p.moveZeroes(nums)
print(nums)