import collections
import heapq
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.defaultdict(tuple)
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = (1, i, i)
            else:
                count[num] = (count[num][0] + 1, count[num][1], i)
        heap = [(-times, end - start + 1) for times, start, end in count.values()]
        heapq.heapify(heap)
        return heapq.heappop(heap)[1]
nums = [1,2,2,3,1,4,2]
p = Solution()
print(p.findShortestSubArray(nums))