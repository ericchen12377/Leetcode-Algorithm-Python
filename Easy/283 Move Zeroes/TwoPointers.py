class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(N):
            if nums[i] != 0:
                continue
            j = i + 1
            while j < N:
                if nums[j] == 0:
                    j += 1
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                break
            if j == N:
                break

nums = [0,1,0,3,12]
p = Solution()
p.moveZeroes(nums)
print(nums)