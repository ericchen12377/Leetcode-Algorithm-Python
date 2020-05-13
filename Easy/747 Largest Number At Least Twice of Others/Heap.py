import heapq
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        largest, ind = heapq.heappop(heap)
        if largest <= 2 * heapq.heappop(heap)[0]:
            return ind
        return -1
