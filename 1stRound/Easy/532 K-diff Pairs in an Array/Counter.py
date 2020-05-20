import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        counter = collections.Counter(nums)
        for num in set(nums):
            if k > 0 and num + k in counter:
                answer += 1
            if k == 0 and counter[num] > 1:
                answer += 1
        return answer
