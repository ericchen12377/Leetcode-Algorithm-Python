import numpy as np
import heapq
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        N = len(nums)
        res = [""] * N
        count = 1
        while heap:
            num, i = heapq.heappop(heap)
            if count == 1:
                res[i] = "Gold Medal"
            elif count == 2:
                res[i] = "Silver Medal"
            elif count == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(count)
            count += 1
        return res
