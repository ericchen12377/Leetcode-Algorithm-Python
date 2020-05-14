import collections
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = dict(), dict()
        count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
        degree = max(count.values())
        res = float("inf")
        for num, c in count.items():
            if c == degree:
                res = min(res, right[num] - left[num] + 1)
        return res
nums = [1,2,2,3,1,4,2]
p = Solution()
print(p.findShortestSubArray(nums))