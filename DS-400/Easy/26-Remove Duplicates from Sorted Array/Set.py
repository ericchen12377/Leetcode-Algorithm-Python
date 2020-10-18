class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)


nums = [1,1,2]
p = Solution()
print(p.removeDuplicates(nums))