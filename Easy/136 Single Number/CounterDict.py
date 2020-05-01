import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        return count.most_common()[-1][0]
p = Solution()
nums = [4,1,2,1,2]
print(p.singleNumber(nums))