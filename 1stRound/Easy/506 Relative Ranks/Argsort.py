import numpy as np
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = np.argsort(np.array(nums))[::-1]
        N = len(nums)
        res = list(map(str, ranks))
        for r in range(N):
            if r == 0:
                res[ranks[0]] = "Gold Medal"
            elif r == 1:
                res[ranks[1]] = "Silver Medal"
            elif r == 2:
                res[ranks[2]] = "Bronze Medal"
            else:
                res[ranks[r]] = str(r + 1)
        return res
nums = [5,6,7,3,4,1,2]
p = Solution()
print(p.findRelativeRanks(nums))