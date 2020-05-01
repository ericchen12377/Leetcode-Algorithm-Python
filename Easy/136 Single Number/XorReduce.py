from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)
p = Solution()
nums = [4,1,2,1,2]
print(p.singleNumber(nums))