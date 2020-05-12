from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num + 1 in counter: #check neighbour
                longest = max(longest, counter[num] + counter[num + 1]) #check longest
        return longest
nums = [1,3,2,2,5,2,3,7]
p = Solution()
print(p.findLHS(nums))