class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        



nums = [4,5,6,7,0,1,2]
target = 0
p = Solution()
print()