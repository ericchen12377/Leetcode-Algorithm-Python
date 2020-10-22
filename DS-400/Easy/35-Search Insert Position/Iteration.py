class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        i = 0
        while(i <= size-1):
            if nums[i] >= target:
                return i
            elif nums[i] < target:
                i += 1
        
        if i == size:
            return size
        else:
            return 0

nums = [1,3,5,6]
target = 5
p = Solution()
print(p.searchInsert(nums, target))