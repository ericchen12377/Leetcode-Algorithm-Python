import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        res = 0
        for num in count.keys():
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
        return res
nums = [1,3,2,2,5,2,3,7]
p = Solution()
print(p.findLHS(nums))